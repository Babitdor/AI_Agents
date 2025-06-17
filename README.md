# AI_Agents

# Personal Knowledge Assistant
This project is a Personal Knowledge Assistant that allows you to interact with your own PDF documents using natural language questions. The assistant parses, chunks, embeds, indexes, and retrieves relevant information from your uploaded PDFs, then generates precise and informative answers using an LLM.

## Features
Upload a PDF and ask questions about its contents.
Automatic text extraction, chunking, and embedding.
Fast similarity search using FAISS.
Answer generation using Ollama with the mistral:latest model.
Modular, node-based RAG pipeline with LangGraph.

## Project Structure

```bash
Agents/
  PersonalKnowledgeAssistant/
    app.py               # Streamlit UI for PDF Q&A
    retriever.py         # RAG pipeline logic (nodes, state, retrieval)
    tools.py             # Utility functions (PDF parsing, LLM answer)
    requirement.txt      # Python dependencies
MCPs/
  TemplateMCP.py         # Example MCP agent (Weather Service)
```

## Getting Started

1. Setup a Python environment using 
```bash
    python -m venv venv
```

2. Install Dependencies
Make sure you have Python 3.10+ installed.

Install required packages:
```bash
    pip install -r requirement.txt
```

2. Run the Assistant
Start the Streamlit app:
```bash
    streamlit run app.py
```

3. Usage
Upload a PDF file.
Enter your question about the PDF.
Get an answer generated from the document's content.
