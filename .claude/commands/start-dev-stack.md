# Start Development Stack

Starts both the frontend (MkDocs) and backend (FastAPI) servers for local development.

## Commands

### Terminal 1: Frontend
```bash
mkdocs serve
```
Access at: `http://127.0.0.1:8000`

### Terminal 2: Backend
```bash
python backend/app.py
```
API available at: `http://127.0.0.1:8001`

## Requirements

- Virtual environment activated: `source venv/bin/activate`
- `.env` file with `OPENAI_API_KEY` configured
- ChromaDB already initialized (run `python scripts/build_vectordb.py` first)

## Health Check

Verify backend is running:
```bash
curl http://127.0.0.1:8001/api/health
```

Expected response:
```json
{"status": "ok", "vectordb": "connected"}
```

## Testing Endpoints

### Chatbot (streaming)
```bash
curl -X POST http://127.0.0.1:8001/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [{"role": "user", "content": "What is a CT chest PE protocol?"}],
    "current_page": ""
  }'
```

### Protocoller
```bash
curl -X POST http://127.0.0.1:8001/api/protocoller \
  -H "Content-Type: application/json" \
  -d '{"indication": "Suspect pulmonary embolism"}'
```
