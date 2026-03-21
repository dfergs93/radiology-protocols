# Project TODO

## 1. CT Protocol Accuracy (Highest Priority)
Focus areas: **cardiac**, **vascular**, **chest**

### Cardiac Protocols
- [ ] Audit and fix injection parameters (contrast agent, volume, flow rate, trigger timing)
- [ ] Fix Mermaid Gantt timing diagrams
- [ ] Fix acquisition series (series names, phases, coverage)

### Vascular Protocols
- [ ] Audit and fix injection parameters
- [ ] Fix Mermaid Gantt timing diagrams
- [ ] Fix acquisition series

### Chest Protocols
- [ ] Audit and fix injection parameters
- [ ] Fix Mermaid Gantt timing diagrams
- [ ] Fix acquisition series

---

## 2. Chatbot Improvements

- [x] Reduce response verbosity — tighten system prompt or add length constraints
- [ ] Improve RAG retrieval quality — reduce irrelevant protocols entering the context window (better chunking, metadata filtering, or re-ranking)
- [ ] Improve handling of advanced/compound queries
- [ ] Fix streaming UI/UX issues
- [ ] **Research spike:** Explore MCP server architecture as an alternative to current ChromaDB RAG — LLM converts queries to structured DB lookups rather than semantic vector search

---

## 3. Protocol Comparison UI

- [x] Hide/filter scout series from the acquisition comparison display
- [ ] Add diff/highlight view to surface differences between selected protocols
- [ ] Add shareable comparison links (encode selected protocols in URL)
- [ ] Add "combination" view showing how two protocols could be merged or run together

---

## 4. Protocoller Improvements

- [ ] Fix custom protocol Gantt diagram accuracy (timing phases are wrong/incomplete)
- [ ] Exclude scout series from custom protocol acquisition output

---

## 5. Protocol Submission Form (New Feature)

- [x] Design API endpoints for protocol creation and editing (`POST /api/protocols`, `PUT /api/protocols/:id`)
- [x] Build web form UI for submitting new protocols
- [ ] Build web form UI for editing existing protocols
- [x] Add server-side validation for protocol structure and required fields
- [ ] Add review/approval step (initially just for solo author; extendable to team workflow later)

---

## 6. Backend Tests

- [ ] Set up pytest with a test configuration
- [ ] Write tests for `GET /api/health`
- [ ] Write tests for `POST /api/chat` (RAG retrieval + streaming)
- [ ] Write tests for `POST /api/protocoller` (protocol selection + custom protocol output)
- [ ] Write tests for guideline calculators in `guideline_tools.py`

---

## 7. Deployment

- [ ] Evaluate alternatives to Render for backend (slow cold starts) — candidates: Railway, Fly.io, VPS
- [ ] Plan hospital network deployment architecture
- [ ] Add authentication / access control (required for hospital deployment)
- [ ] Research on-premise LLM options to replace OpenAI API calls for hospital deployment (Ollama, vLLM, local embeddings)

---

## 8. Infrastructure / Tooling

- [ ] Pin dependency versions in `backend/requirements.txt`
- [ ] Move hard-coded CORS origins and API URLs to environment variables
