# Rebuild Vector Database

Rebuilds the ChromaDB vector database and protocol index from all CT protocol markdown files.

## Command

```bash
python scripts/build_vectordb.py
```

## When to Use

- After adding new protocol markdown files to `docs/ct/`
- After significantly editing existing protocol content
- Before testing the chatbot or protocoller endpoints
- When protocol titles or categories change

## What It Does

1. Scans `docs/ct/**/*.md` for all protocol files
2. Extracts title, category, and indications (from CSV if available)
3. Generates embeddings using OpenAI `text-embedding-3-small`
4. Stores embeddings in `backend/chroma_db/`
5. Writes `backend/protocol_index.json` for the Protocoller endpoint

## Requirements

- `.env` file with `OPENAI_API_KEY` configured
- Virtual environment activated: `source venv/bin/activate`
- Optional: `csv/protocols.csv` with `protocol_name` and `clinical_indications` columns for enhanced indications
