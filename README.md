# Radiology Protocol Manager & Guidelines Database

A centralized, web-based platform for managing radiology protocols and clinical guidelines, featuring an AI-powered RAG (Retrieval-Augmented Generation) assistant.

![Status](https://img.shields.io/badge/Status-Active-success)
![Stack](https://img.shields.io/badge/Stack-MkDocs%20%7C%20FastAPI%20%7C%20OpenAI-blue)

## 📖 Overview

This project serves as a comprehensive knowledge base for radiology, combining:
1.  **Protocol Management:** Detailed CT/MRI protocols with technical parameters.
2.  **Clinical Guidelines:** Evidence-based decision support (Fleischner, Lung-RADS, LI-RADS, etc.).
3.  **AI Assistant:** A context-aware chatbot that answers clinical questions using the indexed guidelines as a knowledge source.

The frontend is built with **MkDocs (Material Theme)** for a fast, searchable, and responsive UI. The backend uses **FastAPI** + **ChromaDB** + **OpenAI** to power the RAG chatbot.

---

## 🛠 Project Structure

```
protocol_manager/
├── backend/                 # RAG Chatbot API
│   ├── app.py              # FastAPI application & logic
│   └── chroma_db/          # Vector database storage
├── docs/                    # Content source files
│   ├── ct/                 # CT Protocols (Markdown)
│   ├── guidelines/         # Clinical Guidelines (Markdown)
│   ├── javascripts/        # Custom frontend logic (Chatbot UI, etc.)
│   └── custom_css/         # styling overrides
├── scripts/                 # Utility scripts
│   └── build_vectordb.py   # Ingests guidelines into Vector DB
└── mkdocs.yml              # Site configuration
```

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.9+**
- **OpenAI API Key** (for chatbot functionality)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/dfergs93/protocol_manager.git
    cd protocol_manager
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install mkdocs-material fastapi uvicorn openai chromadb python-dotenv
    ```

4.  **Configure Environment:**
    Create a `.env` file in the root directory:
    ```env
    OPENAI_API_KEY=sk-your-key-here
    ```

### Running the Application

To run the full stack, you need two terminal windows:

**Terminal 1: Frontend (Documentation Site)**
```bash
mkdocs serve
# Access at http://127.0.0.1:8000/radiology-protocols/
```

**Terminal 2: Backend (AI Chatbot API)**
```bash
python backend/app.py
# API runs at http://127.0.0.1:8001
```

---

## 🤖 RAG Chatbot Implementation

The AI assistant uses a **Retrieval-Augmented Generation (RAG)** architecture:

1.  **Ingestion:** The `scripts/build_vectordb.py` script scans `docs/ct` and `docs/guidelines`, chunks the Markdown content, extracts metadata (titles/categories), and generates embeddings using OpenAI (`text-embedding-3-small`). These are stored in a local **ChromaDB**.
2.  **Retrieval:** When a user asks a question, the backend searches ChromaDB for the most relevant document chunks.
3.  **Generation:** The retrieved text is injected into a system prompt for GPT-4o-mini, which answers the user's question citing the specific guidelines.

**To rebuild the knowledge base:**
```bash
# Run this whenever you add/edit markdown files
python scripts/build_vectordb.py
```

---

## 🔮 Future Directions

### Priority Items:

1.  **Guideline Optimziation**
    -   Improve guideline queries by directing them to python functions (e.g. Fleischner nodule size calculator, LI-RADS risk calculator, etc.). 
    -   Place these calculators on the guidelines index.md for quick access
2.  **Protocoller**
    -   Add a protocol interface where the user puts in a clinical indication and the top options for protocols are displayed and compared. 
    -   If necessary, a custom protocol could be created and suggested
3.  **MRI Protocols**
    -   Add MRI Protocols starting with Cardiac

### All Planned Features:

1.  **Expanded Content Coverage:**
    -   **MRI Protocols**
        -   Add MRI Protocols starting with Cardiac
        -   Build a cardiac protocol builder to help understand protocolling
    -   **Guidelines**
        -   Convert guidelines into markdown for ease of reading and RAG implementation
        -   Add more specialty-specific guidelines (Neuroradiology, MSK).

2.  **Advanced Chatbot Capabilities:**
    -   **Chatbot Server**
        -   Add a chatbot server to run locally or on institutional servers
    -   **Guideline Optimziation**
        -   Improve guideline queries by directing them to python functions (e.g. Fleischner nodule size calculator, LI-RADS risk calculator, etc.). 
        -   Place these calculators on the guidelines index.md for quick access
    -   **Calculator Integration:** Allow the bot to perform calculations (e.g., adrenal washout % or creatinine clearance) directly.
    -   **Protocol Comparison Improvements:**
        -   Add a protocoller interface to query protocolling questions and automatically generate comparisons and give suggestions for complex protocol questions
    -   **Protocoller**
        -   Add a protocol interface where the user puts in a clinical indication and the top options for protocols are displayed and compared. 
        -   If necessary, a custom protocol could be created and suggested

3.  **Deployment & Access:**
    -   Dockerize the application for easy deployment on institutional intranets.
    -   Implement user authentication (SSO/LDAP) for secure access.

4.  **Protocol Optimization:**
    -   Link protocols directly to scanner export files.
    -   Track Protocol version history (Git-based versioning is already implicit).

---

## 🤝 Contributing

1.  Create a new branch: `git checkout -b feature/new-guideline`.
2.  Add your markdown file to `docs/guidelines/`.
3.  Rebuild the vector DB to test searchability.
4.  Submit a Pull Request.
