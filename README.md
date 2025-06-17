# AI_Agents


# Personal Knowledge Assistant
A Streamlit-based AI assistant that lets you upload a PDF and ask questions about its content using Retrieval-Augmented Generation (RAG) techniques. The assistant parses, chunks, embeds, indexes, and retrieves relevant information from your PDF, then generates precise answers using an LLM.

Features
Upload any PDF and interactively ask questions about its content.
Uses state-of-the-art embedding models and FAISS for semantic search.
Generates answers using the Ollama LLM API (Mistral model).
Modular, node-based RAG pipeline using LangGraph and LangChain.
Project Structure
Getting Started
1. Install Dependencies
Install Python 3.10+ and run:

2. Start Ollama
Make sure Ollama is installed and running with the mistral model:

3. Run the App
4. Usage
Upload a PDF file in the web UI.
Enter your question about the PDF content.
Wait for the assistant to process and answer.
How It Works
PDF Parsing: Extracts text from the uploaded PDF (extract_text_from_pdf).
Chunking: Splits text into manageable chunks.
Embedding: Converts chunks into vector embeddings using Sentence Transformers.
Indexing: Builds a FAISS index for efficient similarity search.
Retrieval: Finds the most relevant chunks for your query.
Answer Generation: Sends context and question to Ollama LLM (generate_answer).
Customization
Swap out the embedding model or LLM in retriever.py and tools.py.
Adjust chunk size and overlap for different document types.
Example MCP
See TemplateMCP.py for an example of a Multi-Component Process (MCP) for weather services
