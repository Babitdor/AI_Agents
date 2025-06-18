import os
import ast
import tempfile
import requests
from git import Repo
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import PythonCodeTextSplitter
import numpy as np
import faiss
import ollama

model = SentenceTransformer("all-MiniLM-L6-v2")


def clone_repo(repo_url: str) -> str:
    """
    Clones a repository using a repo url

    Args: repo_url: string

    returns: path of the cloned repo directory
    """
    temp_dir = tempfile.mkdtemp()
    Repo.clone_from(repo_url, temp_dir)
    return temp_dir


def extract_code_chunks(repo_path):
    splitter = PythonCodeTextSplitter(chunk_size=500, chunk_overlap=50)

    code_chunks = []

    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    source_code = f.read()
                    chunks = splitter.split_text(source_code)
                    code_chunks.extend(chunks)

    return code_chunks


def embed_chunks(chunks):
    embeddings = np.array(model.encode(chunks))
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    return index, chunks, embeddings


def retrieve_chunks(query, chunks, embeddings, k=5):
    query_emb = model.encode([query])
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    _, indices = index.search(query_emb, k)

    return [chunks[i] for i in indices[0]]


def generate_answer(context, query, model_name="mistral:latest"):
    prompt = f""" You are a knowledgeable and precise coding assistant. Your job is to help developers understand and improve codebases. Given a code snippet, file, or repository context, you should:

Explain what the code does in simple, clear terms.

Answer specific technical questions accurately.

Suggest improvements following best practices.

Spot bugs or edge cases and offer fixes.

Adapt explanations to the user`s experience level when asked.

Always be concise, factual, and avoid making assumptions if the context is unclear. If the question involves a larger codebase, be sure to refer only to what`s provided unless told otherwise. 
    
    
Based on the given context {context} and the Question: {query}


Answer:"""

    response = ollama.chat(
        model="qwen2.5-coder:1.5b", messages=[{"role": "user", "content": prompt}]
    )

    return response["message"].content
