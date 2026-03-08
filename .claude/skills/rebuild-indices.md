# Rebuild All Indices

Rebuilds both the vector database (for chatbot/protocoller) and the comparison index (for UI).

## Usage

```
/rebuild-indices
```

## What It Does

Runs both scripts in sequence:

1. **Vector Database** (`python scripts/build_vectordb.py`)
   - Scans `docs/ct/**/*.md`
   - Generates embeddings for RAG
   - Updates `backend/chroma_db/` and `backend/protocol_index.json`

2. **Comparison Index** (`python scripts/generate_comparison_index.py`)
   - Parses protocol markdown files
   - Extracts Gantt diagrams, contrast info, series data
   - Updates `docs/javascripts/protocol-comparison-index.json`

## Requirements

- `.env` file with `OPENAI_API_KEY` configured
- Virtual environment activated
- All protocol markdown files are valid

## When to Use

- After bulk editing multiple protocol files
- After reorganizing protocol categories
- When preparing for deployment or testing
- Daily during active protocol development

## Output

Both scripts print progress and completion counts. The skill verifies:
- ✓ All protocols were indexed
- ✓ JSON files are valid
- ✓ No files failed processing

## Troubleshooting

If the vector DB rebuild fails:
- Check that `.env` has a valid `OPENAI_API_KEY`
- Verify markdown files don't have encoding issues
- Review error messages for specific file paths

If the comparison index fails:
- Ensure Mermaid Gantt syntax is correct in protocols
- Check that Injection Parameters and Series tables exist
- Validate table formatting (pipes and separators)
