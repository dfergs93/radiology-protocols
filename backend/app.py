from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import chromadb
from openai import OpenAI
import os
import json
from dotenv import load_dotenv
import asyncio

load_dotenv()

app = FastAPI()

# Get absolute path to backend directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# CORS configuration
ALLOWED_ORIGINS = [
    "http://localhost:8000", 
    "http://127.0.0.1:8000", 
    "http://127.0.0.1:8000/radiology-protocols/",
    "http://localhost:8002",
    "http://127.0.0.1:8002",
    "https://dfergs93.github.io",
    "https://dfergs93.github.io/radiology-protocols/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize clients
openai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

try:
    chroma_client = chromadb.PersistentClient(path=os.path.join(BASE_DIR, "chroma_db"))
    collection = chroma_client.get_collection("protocols")
    print("✓ Connected to ChromaDB")
except Exception as e:
    print(f"✗ ChromaDB error: {e}")
    print("Run: python scripts/build_vectordb.py")
    collection = None

# Load protocol index
PROTOCOL_INDEX = []
try:
    # Use absolute path for protocol_index.json
    index_path = os.path.join(BASE_DIR, 'protocol_index.json')
    with open(index_path, 'r') as f:
        PROTOCOL_INDEX = json.load(f)
    print(f"✓ Loaded {len(PROTOCOL_INDEX)} protocols for Protocoller")
except Exception as e:
    print(f"✗ Failed to load protocol_index.json: {e}")

class ProtocollerRequest(BaseModel):
    indication: str

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatQuery(BaseModel):
    messages: list[ChatMessage]
    current_page: str = ""

def get_embedding(text):
    """Get embedding from OpenAI"""
    response = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

@app.post("/api/protocoller")
async def protocol_recommendation(request: ProtocollerRequest):
    """Protocol Recommendation Endpoint"""
    
    indication = request.indication
    print(f"\nProtocoller Request: {indication}")
    
    # Context is the entire protocol index (Title + Indications)
    index_context = ""
    for p in PROTOCOL_INDEX:
        # Include title and indications
        index_context += f"- {p['title']}: {p.get('indications', '')}\n"
    
    # Static part of the prompt
    SYSTEM_PROMPT_TEMPLATE = """You are an expert CT protocol specialist. Suggest existing protocols or create custom protocols by modifying standard protocols to answer specific clinical questions.

    Available Protocols:
    """

    SYSTEM_PROMPT_RULES = """
═══════════════════════════════════════════════════════════════════════════════
CORE PRINCIPLES
═══════════════════════════════════════════════════════════════════════════════

CONTRAST TIMING:
• Arterial: Bolus duration + 5-10s (or bolus tracking, 100-150 HU threshold)
• Portal venous: 45-60s (chest), 70-90s (abdomen/pelvis)
• Nephrographic: 90-100s
• Delayed: 3-10 minutes
• Flow rate: 4-5 mL/s (arterial), 3-4 mL/s (venous), 2-3 mL/s (extended)
• Saline chaser: 20-40 mL at same rate

BOLUS CALCULATION:
1. Estimate scan duration (chest: ~10s, abdomen: ~10s, pelvis: ~7s)
2. Bolus duration = scan duration + 10s buffer
3. Volume = flow rate × bolus duration
4. Max volume: ~150 mL (adjust for renal function)

DECISION RULES:
• Different phases, same region → Multiple acquisitions
• Same phase, extended region → Lengthen bolus, single acquisition  
• Different phases, different regions → Separate targeted acquisitions

WHEN TO CREATE CUSTOM PROTOCOL:
✓ Specific timing/coverage requested not in standard protocols
✓ Clinical question requires modification (extend coverage, add phase, adjust timing)
✗ Standard protocol perfectly matches → recommend existing only

═══════════════════════════════════════════════════════════════════════════════
WORKFLOW
═══════════════════════════════════════════════════════════════════════════════

1. ANALYZE: What pathology? What structures? What phase(s)?
2. SELECT: Closest base protocol
3. DETERMINE STRATEGY:
   - Different phases needed? → Multiple acquisitions
   - Extended coverage needed? → Lengthen bolus if same phase throughout
4. CALCULATE:
   - Scan time → Bolus duration → Volume (rate × duration)
   - Delay based on phase (arterial/venous/delayed)
5. VERIFY: Volume safe? Timing appropriate? Phases justified?

═══════════════════════════════════════════════════════════════════════════════
JSON OUTPUT
═══════════════════════════════════════════════════════════════════════════════

{
  "recommended_protocols": [
    {
      "title": "Exact Title from Available Protocols",
      "reasoning": "Clinical rationale for match"
    }
  ],
  "custom_protocol": {
      "title": "Custom: [Descriptive Name]",
      "description": "Base Protocol: [Standard Protocol]. Modifications: [Changes with justification]",
      "gantt": "gantt\\n    title Timing\\n    dateFormat mm:ss\\n    axisFormat %M:%S\\n    section Contrast\\n    Contrast (100mL @ 4mL/s) : 00:00, 25s\\n    Saline (30mL @ 4mL/s) : 00:25, 8s\\n    section Scan\\n    Acquisition : crit, 00:30, 10s",
      "contrast": {
          "agent": "Isovue 370",
          "volume": "100 mL",
          "flow_rate": "4 mL/s",
          "trigger": "Bolus Tracking | Fixed Delay",
          "timing": "30s (rationale)"
      },
      "series": [
          {
              "name": "Phase Name",
              "thickness": "0.625-1.25mm (CTA) | 2.5-5mm (routine)",
              "coverage": "Anatomic landmarks",
              "delay": "30s | Non-contrast"
          }
      ]
  }
}

GANTT RULES:
- Calculate precisely: Contrast end = volume/rate, Saline start = contrast end
- Scan start = clinical delay (arterial: ~30s, venous: ~70s)
- Multiple acquisitions: add multiple scan lines with different delays
- Use \\n for newlines, mm:ss format

RULES:
- Always include recommended_protocols (1-3 matches)
- Only include custom_protocol if modification needed
- Gantt timing must match contrast/series delays exactly
- Return ONLY valid JSON, no markdown

EXAMPLES:

Simple match → recommended_protocols only
Specific timing → custom_protocol with calculated gantt
Multiple phases → custom_protocol with multiple series entries
"""
    system_prompt = SYSTEM_PROMPT_TEMPLATE + index_context + SYSTEM_PROMPT_RULES

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Clinical Indication: {indication}"}
    ]
    
    try:
        print("Calling OpenAI for Protocoller...")
        response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.1,
            response_format={"type": "json_object"}
        )
        
        content = response.choices[0].message.content
        result = json.loads(content)
        
        # Hydrate recommended protocols with filepath from index
        hydrated_recommendations = []
        for rec in result.get('recommended_protocols', []):
            # Find matching protocol in index
            match = next((p for p in PROTOCOL_INDEX if p['title'] == rec['title']), None)
            if match:
                rec['filepath'] = match['filepath']
                hydrated_recommendations.append(rec)
        
        result['recommended_protocols'] = hydrated_recommendations
        
        return result

    except Exception as e:
        print(f"Protocoller Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/chat")
async def chat(query: ChatQuery):
    """RAG chatbot endpoint with streaming"""
    
    if not collection:
        raise HTTPException(status_code=500, detail="Vector database not initialized")
    
    # Get the last user message
    last_message = query.messages[-1].content
    
    print(f"\nQuestion: {last_message}")
    
    # Get embedding for the question
    question_embedding = get_embedding(last_message)
    
    # Search vector DB for relevant protocols
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=3
    )
    
    # Build context from retrieved documents
    context_docs = []
    print(f"Retrieved {len(results['documents'][0])} protocols:")
    
    sources = []
    for i, doc in enumerate(results['documents'][0]):
        metadata = results['metadatas'][0][i]
        print(f"  {i+1}. {metadata['title']} (relevance: {1-results['distances'][0][i]:.2f})")
        
        # Add protocol to context
        context_docs.append(f"### Protocol: {metadata['title']}\n{doc[:10000]}")  # First 10000 chars
        
        # Collect sources
        sources.append({
            "title": metadata['title'],
            "filepath": metadata['filepath'],
            "category": metadata['category']
        })
    
    context = "\n\n---\n\n".join(context_docs)
    
    # Build system prompt
    system_prompt = f"""You are an expert radiology assistant specializing in CT imaging protocols and clinical guidelines.

You have access to the following relevant protocols and guidelines:

{context}

Current page: {query.current_page}

Your primary functions:
1. Answer questions about CT protocols (technique, contrast timing, patient preparation)
2. Provide guidance on protocol selection based on clinical indications
3. Reference evidence-based guidelines when appropriate
4. Help compare different protocol approaches
5. Clarify safety considerations (contrast, radiation dose, contraindications)

- **Reasoning Process:**
    1. Identify patient risk factors and nodule characteristics (size, type, multiplicity).
    2. Explicitly state the size category the nodule falls into (e.g., "10 mm is > 8 mm category").
    3. Locate the specific row in the table that matches ALL criteria.
    4. Provide the recommendation from that row.
- **Quote guidelines directly** when available in context
- **Strictly adhere to the provided context.** Do not use outside knowledge if it contradicts the context.
- **Markdown Tabs:** The content contains '===' which denotes tabs (e.g., "Solid nodules" vs "Subsolid nodules"). Read all tabs.
- Reference specific protocols when available
- Use exact numbers and timeframes from retrieved documents
- Distinguish between guideline recommendations and institutional protocols
- Be concise but accurate
- If making a guideline recommendation, provide a sample output that can be pasted into a radiology report.
- Flag safety concerns prominently
- If uncertain or context is incomplete, acknowledge it clearly

Format responses with:
- Clear section headers when appropriate
- Bullet points for lists
- **Bold** for important safety information
- Protocol names in quotes (e.g., "CTA Chest PE Protocol")
You have access to both institutional protocols AND clinical guidelines."""

    # Build messages for OpenAI
    messages = [{"role": "system", "content": system_prompt}]
    
    # Add conversation history (last 6 messages to keep context)
    for msg in query.messages[-6:]:
        messages.append({"role": msg.role, "content": msg.content})
    
    # Streaming generator function
    async def generate_stream():
        try:
            print("Calling OpenAI with streaming...")
            
            # Create streaming response
            stream = openai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                temperature=0.1,
                max_tokens=800,
                stream=True  # Enable streaming
            )
            
            # Send sources first as a special event
            sources_json = json.dumps({"sources": sources})
            yield f"data: {sources_json}\n\n"
            
            # Stream the response content
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    content = chunk.choices[0].delta.content
                    # Send each chunk as Server-Sent Event
                    chunk_json = json.dumps({"content": content})
                    yield f"data: {chunk_json}\n\n"
                    await asyncio.sleep(0)  # Allow other tasks to run
            
            # Send done signal
            yield f"data: {json.dumps({'done': True})}\n\n"
            
            print("Streaming completed\n")
            
        except Exception as e:
            print(f"OpenAI streaming error: {e}")
            error_json = json.dumps({"error": str(e)})
            yield f"data: {error_json}\n\n"
    
    return StreamingResponse(
        generate_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"  # Disable buffering in nginx
        }
    )

@app.get("/api/health")
async def health():
    """Health check endpoint"""
    return {
        "status": "ok",
        "vectordb": "connected" if collection else "not connected"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)