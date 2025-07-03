# Personal Knowledge Assistant
This project is a Personal Knowledge Assistant that allows you to interact with your own PDF documents using natural language questions. The assistant parses, chunks, embeds, indexes, and retrieves relevant information from your uploaded PDFs, then generates precise and informative answers using an LLM.

## Features
Upload a PDF and ask questions about its contents.
Automatic text extraction, chunking, and embedding.
Fast similarity search using FAISS.
Answer generation using Ollama with the mistral:latest model by default.
Flexible LLM support: You can easily swap in other LLMs (e.g., OpenAI, local models, etc.) by modifying the generate_answer function in tools.py.
Modular, node-based RAG pipeline with LangGraph.

## Project Structure

```bash
Agents/
  PersonalKnowledgeAssistant/
    app.py               # Streamlit UI for PDF Q&A
    retriever.py         # RAG pipeline logic (nodes, state, retrieval)
    tools.py             # Utility functions (PDF parsing, LLM answer)
    requirement.txt      # Python dependencies
```

## Getting Started

1. **Start Ollama with a model** (In a separate terminal)

   ```bash
   ollama run mistral
   ```
2. **Setup Python Environment**

   ```bash
   python -m venv venv
   ```
2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**

   ```bash
   streamlit run app.py
   ```

4. **In the app**:

   * Upload a PDF file.
   * Enter your question.
   * Get an answer generated based on the document's content.

---

## 📦 Requirements

* [Ollama](https://ollama.com) installed and running locally.

  * Model: `mistral:latest` pulled (`ollama pull mistral`)
* Python 3.9+
* Required packages listed in `requirements.txt`:

  * `streamlit`, `langgraph`, `sentence-transformers`, `faiss-cpu`, `pymupdf`, `requests`, etc.

---

## 🧩 Code Overview

* `app.py`
  🖼️ Streamlit interface for uploading PDFs and asking questions.

* `retriever.py`
  ⚙️ RAG pipeline with LangGraph: defines `RagState` and all nodes for:

  * Parsing
  * Chunking
  * Embedding
  * Indexing
  * Retrieval
  * Answer generation

* `tools.py`
  🧠 Utility functions:

  * PDF text extraction with PyMuPDF
  * Answer generation via local Ollama HTTP API (e.g., `mistral`, `llama3`, `phi3`)

---

## ⚠️ Note

* Ollama **must be running** locally with the `mistral:latest` model for the app to function.
* You can swap in other supported models by modifying `tools.py`.
