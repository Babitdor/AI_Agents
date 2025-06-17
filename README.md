# AI_Agents

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

4. Requirements
Ollama running locally with the mistral:latest model pulled.
Python packages as listed in requirement.txt.

5. Code Overview
    
   -UI: app.py

   -Streamlit interface for file upload and Q&A.

   -RAG Pipeline: retriever.py
      Contains the RagState and all graph nodes for parsing, chunking, embedding, indexing, retrieval, and answer generation.

   -Tools: tools.py
      Functions for PDF text extraction and answer generation using Ollama or any other LLM you configure.

Note:
You must have Ollama running and the mistral:latest model available locally for answer generation to work.
