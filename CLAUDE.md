# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Project Is

A radiology protocol management platform with two main components:
1. **Frontend**: A MkDocs (Material theme) static site serving CT/MRI protocol documentation with interactive protocol comparison and recommendation.
2. **Backend**: A FastAPI server providing protocol recommendation (Protocoller).

## 
Development Commands

### Running the Stack

Two terminals required:

```bash
# Terminal 1: Frontend (MkDocs dev server)
mkdocs serve
# Accessible at http://127.0.0.1:8000

# Terminal 2: Backend (FastAPI)
python backend/app.py
# API at http://127.0.0.1:8001
```

### Rebuilding the Vector Database

Run this after adding or editing any markdown protocol files in `docs/ct/`:
```bash
python scripts/build_vectordb.py
```
This reads `docs/ct/**/*.md`, embeds each protocol using OpenAI `text-embedding-3-small`, stores in `backend/chroma_db/`, and writes `backend/protocol_index.json`.

Clinical indications can be supplemented from `csv/protocols.csv` (columns: `protocol_name`, `clinical_indications`).

### Regenerating the Comparison Index

Run after editing CT protocol markdown files to update the protocol comparison UI:
```bash
python scripts/generate_comparison_index.py
```
Outputs to `docs/javascripts/protocol-comparison-index.json`.

## Architecture

### Backend API Endpoints (`backend/app.py`)

| Endpoint | Purpose |
|---|---|
| `POST /api/chat` | RAG chatbot — embeds question, retrieves 3 protocol chunks from ChromaDB, streams GPT-4o-mini response |
| `POST /api/protocoller` | Protocol recommendation — GPT-4o selects/creates protocols from clinical indication, returns JSON with recommended protocols + optional custom protocol with Mermaid Gantt |
| `GET /api/health` | Health check |

### Frontend JavaScript (`docs/javascripts/`)

- `chatbot.js` — Chatbot UI, SSE streaming consumer, connects to `/api/chat`
- `protocoller.js` — Protocol recommendation UI, calls `/api/protocoller`, renders Mermaid Gantt diagrams
- `protocol-compare.js` — Side-by-side protocol comparison tool, reads from `protocol-comparison-index.json`
- `protocol-comparison-index.json` — Pre-generated index (Gantt, contrast, series data) for comparison UI

### Protocol Markdown Format

CT protocols in `docs/ct/<category>/<protocol-name>.md` follow a structured template with:
- H1 title (used as protocol name throughout the system)
- Mermaid Gantt diagram (`gantt` inside ` ```mermaid ``` ` block) for contrast timing visualization
- `| Parameter | Value |` table for injection parameters (agent, volume, flow rate, trigger, timing)
- `| Series Name | ... |` table for acquisition series
- `| Series | Phase | Coverage |` table for acquisition summary

The `generate_comparison_index.py` script parses these tables with regex/line-scanning to build the comparison index.

### MkDocs Configuration

- Plugin: `awesome-pages` controls navigation via `.pages` files in subdirectories
- MRI protocols are in `docs/mri/` (newer addition)
- External JS loaded: Mermaid, MathJax, marked.js

### Models Used

- Embeddings: `text-embedding-3-small` (ingestion + query time)
- Chat: `gpt-4o-mini` (RAG chat, streaming)
- Protocoller: `gpt-4o` (protocol recommendation, JSON mode)
