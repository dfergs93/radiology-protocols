from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from pydantic import BaseModel, Field
import chromadb
from openai import OpenAI
import os
import json
import re
import sys
from pathlib import Path
from dotenv import load_dotenv
import asyncio
from typing import Dict, Any, Literal

load_dotenv()

app = FastAPI()

# Get absolute path to backend directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'scripts'))
from protocol_template import PROTOCOL_TEMPLATE
DOCS_CT_DIR = os.path.realpath(os.path.join(PROJECT_ROOT, 'docs', 'ct'))

# CORS configuration
ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8000/radiology-protocols/",
    "https://dfergs93.github.io",
    "https://dfergs93.github.io/radiology-protocols/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    """Return 403 for requests to non-API paths (e.g. path-traversal attempts that
    get URL-normalized outside /api/ before they reach route matching)."""
    if exc.status_code == 404 and not request.url.path.startswith('/api/'):
        return JSONResponse({"detail": "Access denied"}, status_code=403)
    return JSONResponse({"detail": exc.detail}, status_code=exc.status_code)


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

VALID_CATEGORIES = {"Cardiac", "Vascular", "Chest", "Abdomen", "Neuro", "Msk", "Trauma"}

class AcquisitionSummaryRow(BaseModel):
    series: str
    phase: str
    coverage: str

class GanttRow(BaseModel):
    label: str
    duration_seconds: int = Field(gt=0)  # spec requires duration > 0
    type: Literal["contrast", "saline", "scan", "other"]
    start: str  # "00:00" for absolute, "after:<slug>" for dependency

class SeriesRow(BaseModel):
    name: str
    start: str
    end: str
    delay: str
    thickness: str
    notes: str

class PostProcRow(BaseModel):
    plane: str
    acquisition: str
    fov: str
    thickness_increment: str
    kernel: str
    ir_strength: str
    notes: str

class ProtocolGenerateRequest(BaseModel):
    protocol_name: str
    author: str
    last_updated: str
    category: str
    protocol_type: str
    clinical_indications: str
    acquisition_summary: list[AcquisitionSummaryRow]
    patient_positioning: str
    npo_status: str
    premedication: str
    contrast_agent: str
    contrast_volume: str
    contrast_flow_rate: str
    contrast_timing_method: str
    contrast_roi_placement: str
    contrast_trigger: str
    lab_requirements: str
    tech_notes: str
    nursing_notes: str
    radiologist_notes: str
    tips_tricks: str
    safety_renal_function: str
    safety_allergy: str
    gantt_rows: list[GanttRow]
    gantt_raw: str
    series: list[SeriesRow]
    kv: str
    mas: str
    rotation_time: str
    pitch: str
    post_processing: list[PostProcRow]
    additional_recons: str


@app.get("/api/protocols")
async def list_protocols():
    """Return protocol list for submission form dropdown"""
    return PROTOCOL_INDEX


def _parse_protocol_file(content: str) -> dict:
    """Parse a protocol markdown file into structured form data."""
    result = {}

    # Title
    m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    result['protocol_name'] = m.group(1).strip() if m else ''

    # Author and last updated
    m = re.search(r'\*\*Author:\*\*\s*(.+)', content)
    result['author'] = m.group(1).strip() if m else ''
    m = re.search(r'\*\*Last Updated:\*\*\s*(.+)', content)
    result['last_updated'] = m.group(1).strip() if m else ''

    # Footer: Category and Protocol Type
    m = re.search(r'^Category:\s*(.+)$', content, re.MULTILINE)
    result['category'] = m.group(1).strip() if m else ''
    m = re.search(r'^Protocol Type:\s*(.+)$', content, re.MULTILINE)
    result['protocol_type'] = m.group(1).strip() if m else ''

    # Patient prep
    m = re.search(r'\*\*Position:\*\*\s*(.+)', content)
    result['patient_positioning'] = m.group(1).strip() if m else ''
    m = re.search(r'\*\*NPO Status:\*\*\s*(.+)', content)
    result['npo_status'] = m.group(1).strip() if m else ''

    # Premedication
    m = re.search(r'\*\*Premedication[^:]*:\*\*\s*(.+?)(?=\n\s*[-*]|\n\n)', content, re.DOTALL)
    result['premedication'] = m.group(1).strip() if m else ''

    # Clinical indications tab
    m = re.search(r'=== "Clinical Indications"\s*\n(.*?)(?====|\Z)', content, re.DOTALL)
    if m:
        lines = [ln.strip().lstrip('- ').strip() for ln in m.group(1).split('\n')
                 if ln.strip() and not ln.strip().startswith('===')]
        result['clinical_indications'] = '\n'.join(lines)
    else:
        result['clinical_indications'] = ''

    # Acquisition summary table
    summary = []
    in_table = False
    for line in content.split('\n'):
        if '| Series | Phase | Coverage |' in line:
            in_table = True
            continue
        if in_table and '|:---' in line:
            continue
        if in_table and line.strip() and line.strip().startswith('|'):
            cells = [c.strip() for c in line.split('|') if c.strip()]
            if len(cells) >= 3:
                summary.append({'series': cells[0], 'phase': cells[1], 'coverage': cells[2]})
        elif in_table:
            break
    result['acquisition_summary'] = summary

    # Injection parameters table
    contrast = {}
    in_table = False
    for line in content.split('\n'):
        if '| Parameter | Value |' in line:
            in_table = True
            continue
        if in_table and '|---' in line:
            continue
        if in_table and line.strip() and line.strip().startswith('|'):
            cells = [c.strip() for c in line.split('|') if c.strip()]
            if len(cells) >= 2:
                param, value = cells[0].lower(), cells[1]
                if 'agent' in param:
                    contrast['agent'] = value
                elif 'volume' in param:
                    contrast['volume'] = value
                elif 'flow rate' in param:
                    contrast['flow_rate'] = value
                elif 'timing' in param:
                    contrast['timing_method'] = value
                elif 'roi' in param:
                    contrast['roi_placement'] = value
                elif 'trigger' in param:
                    contrast['trigger'] = value
        elif in_table:
            break
    result['contrast_agent'] = contrast.get('agent', '')
    result['contrast_volume'] = contrast.get('volume', '')
    result['contrast_flow_rate'] = contrast.get('flow_rate', '')
    result['contrast_timing_method'] = contrast.get('timing_method', '')
    result['contrast_roi_placement'] = contrast.get('roi_placement', '')
    result['contrast_trigger'] = contrast.get('trigger', '')

    # Lab requirements
    m = re.search(r'=== "Lab Requirements"\s*\n(.*?)(?====|\Z)', content, re.DOTALL)
    result['lab_requirements'] = m.group(1).strip() if m else ''

    # Special notes tabs
    for tab_name, key in [
        ("Technologist Notes", "tech_notes"),
        ("Nursing Notes", "nursing_notes"),
        ("Radiologist Notes", "radiologist_notes"),
        ("Tips & Tricks", "tips_tricks"),
    ]:
        m = re.search(rf'=== "{re.escape(tab_name)}"\s*\n(.*?)(?====|\Z)', content, re.DOTALL)
        result[key] = m.group(1).strip() if m else ''

    # Safety fields
    m = re.search(r'\*\*Renal Function:\*\*\s*(.+)', content)
    result['safety_renal_function'] = m.group(1).strip() if m else ''
    m = re.search(r'\*\*Allergy[^:]*:\*\*\s*(.+)', content)
    result['safety_allergy'] = m.group(1).strip() if m else ''

    # Gantt: raw mermaid content
    m = re.search(r'```mermaid\s*\n(.*?)```', content, re.DOTALL)
    result['gantt_raw'] = m.group(1).strip() if m else ''

    # Series acquisition table
    series = []
    in_table = False
    for line in content.split('\n'):
        if '| Series Name |' in line or '| **Series Name** |' in line:
            in_table = True
            continue
        if in_table and '|:---' in line:
            continue
        if in_table and line.strip() and line.strip().startswith('|'):
            cells = [c.strip().replace('**', '') for c in line.split('|') if c.strip()]
            if len(cells) >= 5:
                series.append({
                    'name': cells[0], 'start': cells[1], 'end': cells[2],
                    'delay': cells[3], 'thickness': cells[4],
                    'notes': cells[5] if len(cells) > 5 else ''
                })
        elif in_table:
            in_table = False
    result['series'] = series

    # Technical parameters
    tech = {}
    in_table = False
    for line in content.split('\n'):
        if '=== "Technical Parameters"' in line:
            in_table = True
            continue
        if in_table and '| Parameter | Value |' in line:
            continue
        if in_table and '|---' in line:
            continue
        if in_table and line.strip().startswith('|'):
            cells = [c.strip() for c in line.split('|') if c.strip()]
            if len(cells) >= 2:
                tech[cells[0].lower()] = cells[1]
        elif in_table and line.strip() and not line.strip().startswith('|'):
            in_table = False
    result['kv'] = tech.get('kv', '')
    result['mas'] = tech.get('mas', '')
    result['rotation_time'] = tech.get('rotation time', '').replace('s', '').strip()
    result['pitch'] = tech.get('pitch', '')

    # Post-processing table
    post_proc = []
    in_table = False
    for line in content.split('\n'):
        if '=== "Post-Processing"' in line:
            in_table = True
            continue
        if in_table and '| Plane |' in line:
            continue
        if in_table and '|---' in line:
            continue
        if in_table and line.strip().startswith('|'):
            cells = [c.strip() for c in line.split('|') if c.strip()]
            if len(cells) >= 6:
                post_proc.append({
                    'plane': cells[0], 'acquisition': cells[1], 'fov': cells[2],
                    'thickness_increment': cells[3], 'kernel': cells[4],
                    'ir_strength': cells[5], 'notes': cells[6] if len(cells) > 6 else ''
                })
        elif in_table and line.strip() and not line.strip().startswith('|'):
            in_table = False
    result['post_processing'] = post_proc

    result['additional_recons'] = ''  # Best effort; hard to extract reliably

    return result


def _slugify(text: str) -> str:
    return re.sub(r'[^a-z0-9]+', '_', text.lower()).strip('_')

def _unique_slugs(rows: list) -> list:
    slugs = []
    seen: dict = {}
    for row in rows:
        base = _slugify(row.label)
        if base in seen:
            seen[base] += 1
            slugs.append(f"{base}_{seen[base]}")
        else:
            seen[base] = 1
            slugs.append(base)
    return slugs

def _seconds_to_mmss(seconds: int) -> str:
    return f"{seconds // 60:02d}:{seconds % 60:02d}"

def _build_gantt_content(rows: list, gantt_raw: str) -> str:
    if not rows:
        return gantt_raw
    slugs = _unique_slugs(rows)
    type_to_class = {"contrast": "active", "saline": "active", "scan": "crit", "other": ""}
    lines = ["section Injection"]
    scan_section_added = False
    for row, slug in zip(rows, slugs):
        cls = type_to_class.get(row.type, "")
        duration_str = _seconds_to_mmss(row.duration_seconds)
        start_str = row.start.replace("after:", "after ") if row.start.startswith("after:") else row.start
        cls_part = f"{cls}, " if cls else ""
        if row.type == "scan" and not scan_section_added:
            lines.append("    section Scan")
            scan_section_added = True
        lines.append(f"      {row.label} :{cls_part}{slug}, {start_str}, {duration_str}")
    return "\n    ".join(lines)

def _build_acquisition_summary_table(rows: list) -> str:
    header = "        | Series | Phase | Coverage |\n        |:---|:---|:---|\n"
    body = "".join(f"        | {r.series} | {r.phase} | {r.coverage} |\n" for r in rows)
    return header + body

def _build_series_table(rows: list) -> str:
    header = "    | Series Name | Start | End | Delay | Thickness | Notes |\n    |:---|:---|:---|:---|:---|:---|\n"
    body = "".join(
        f"    | **{r.name}** | {r.start} | {r.end} | {r.delay} | {r.thickness} | {r.notes} |\n"
        for r in rows
    )
    return header + body

def _build_contrast_section(req) -> str:
    # IMPORTANT: The template has 4 spaces before {contrast_section}.
    # Python's .format() prepends those 4 spaces to the FIRST line only.
    # So use 0 spaces on the first line and 4 spaces on subsequent lines.
    lab = req.lab_requirements or "N/A"
    return (
        '=== "Injection Parameters"\n\n'
        '        | Parameter | Value |\n'
        '        |-----------|-------|\n'
        f'        | Agent | {req.contrast_agent} |\n'
        f'        | Volume | {req.contrast_volume} |\n'
        f'        | Flow Rate | {req.contrast_flow_rate} |\n'
        f'        | Timing Method | {req.contrast_timing_method} |\n'
        f'        | ROI Placement | {req.contrast_roi_placement} |\n'
        f'        | Trigger (HU) | {req.contrast_trigger} |\n\n'
        '    === "Lab Requirements"\n\n'
        f'        {lab}'
    )

def _build_postproc_table(rows: list) -> str:
    header = "    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |\n    |:---|:---|:---|:---|:---|:---|:---|\n"
    body = "".join(
        f"    | {r.plane} | {r.acquisition} | {r.fov} | {r.thickness_increment} | {r.kernel} | {r.ir_strength} | {r.notes} |\n"
        for r in rows
    )
    return header + body

def _format_notes(text: str, indent: str = "        ") -> str:
    if not text:
        return f"{indent}N/A"
    return "\n".join(f"{indent}{line}" for line in text.split('\n'))

def _format_indications(text: str) -> str:
    if not text:
        return "        - N/A"
    return "\n".join(f"        - {line.strip()}" for line in text.split('\n') if line.strip())

def _format_premedication(text: str) -> str:
    if not text:
        return ""
    return f"    - **Premedication:** {text}"


@app.post("/api/protocols/generate")
async def generate_protocol(req: ProtocolGenerateRequest):
    """Generate protocol markdown from form fields"""
    if req.category not in VALID_CATEGORIES:
        raise HTTPException(
            status_code=422,
            detail=[{"loc": ["body", "category"], "msg": f"Must be one of {sorted(VALID_CATEGORIES)}", "type": "value_error"}]
        )
    if not req.clinical_indications.strip():
        raise HTTPException(
            status_code=422,
            detail=[{"loc": ["body", "clinical_indications"], "msg": "At least one clinical indication required", "type": "value_error"}]
        )

    gantt_content = _build_gantt_content(req.gantt_rows, req.gantt_raw)
    additional_recons_section = req.additional_recons.strip() if req.additional_recons.strip() else ""

    markdown = PROTOCOL_TEMPLATE.format(
        protocol_name=req.protocol_name,
        last_updated=req.last_updated,
        author=req.author,
        acquisition_summary_table=_build_acquisition_summary_table(req.acquisition_summary),
        clinical_indications_formatted=_format_indications(req.clinical_indications),
        patient_positioning=req.patient_positioning,
        npo_status=req.npo_status,
        premedication_section=_format_premedication(req.premedication),
        contrast_section=_build_contrast_section(req),
        tech_notes_formatted=_format_notes(req.tech_notes),
        nursing_notes_formatted=_format_notes(req.nursing_notes),
        safety_renal_function=req.safety_renal_function,
        safety_allergy_check=req.safety_allergy,
        radiologist_notes_formatted=_format_notes(req.radiologist_notes),
        artifact_tip_formatted=_format_notes(req.tips_tricks),
        gantt_content=gantt_content,
        series_table=_build_series_table(req.series),
        kv=req.kv,
        mas=req.mas,
        rotation_time=req.rotation_time,
        pitch=req.pitch,
        postproc_table=_build_postproc_table(req.post_processing),
        additional_recons_section=additional_recons_section,
        category=req.category,
        protocol_type=req.protocol_type,
    )

    return {"markdown": markdown}


@app.get("/api/protocols/{filepath:path}")
async def load_protocol(filepath: str):
    """Load and parse a protocol file for form pre-population"""
    # Resolve and validate path is inside docs/ct/
    candidate = os.path.realpath(os.path.join(PROJECT_ROOT, 'docs', filepath))
    if not candidate.startswith(DOCS_CT_DIR + os.sep) and candidate != DOCS_CT_DIR:
        raise HTTPException(status_code=403, detail="Access denied")
    if not os.path.isfile(candidate):
        raise HTTPException(status_code=404, detail="Protocol not found")

    with open(candidate, 'r', encoding='utf-8') as f:
        content = f.read()

    return _parse_protocol_file(content)


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

RESPONSE STYLE:
- Lead with the direct answer. No preamble.
- Keep responses short — 2-4 sentences or a tight bullet list unless the question genuinely requires more.
- Use headers and multi-section formatting only for complex multi-part questions.
- Do not restate the question or add closing summaries.

CONTENT RULES:
- Strictly adhere to the provided context. Do not use outside knowledge if it contradicts the context.
- Use exact numbers and timeframes from retrieved documents.
- Quote guidelines directly when available.
- **Markdown Tabs:** The content contains '===' which denotes tabs (e.g., "Solid nodules" vs "Subsolid nodules"). Read all tabs before answering.
- Distinguish between guideline recommendations and institutional protocols.
- Flag **safety concerns** prominently.
- If uncertain or context is insufficient, say so briefly.
- For guideline recommendations, include a one-line report phrase that can be copy-pasted.

FORMAT:
- Bullet points for lists; **bold** for critical safety info; protocol names in quotes.
- For nodule/guideline queries: state the size category, match to the correct table row, give the recommendation."""

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