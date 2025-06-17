from typing import TypedDict, List, Optional
from langchain_core.runnables import RunnableLambda
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from tools import extract_text_from_pdf, generate_answer


class RagState(TypedDict):
    file: str
    raw_text: Optional[str]
    chunks: List[str]
    embeddings: Optional[List[List[float]]]
    index: Optional[faiss.IndexFlatL2]
    query: str
    retrieved_chunks: List[str]
    answer: Optional[str]


model = SentenceTransformer("all-MiniLM-L6-v2")


# Nodes
def parse_pdf_node(state: RagState):
    text = extract_text_from_pdf(state["file"])
    return RagState({**state, "raw_text": text})


def chunk_text_node(state: RagState):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(state["raw_text"])
    return RagState({**state, "chunks": chunks})


def embed_node(state: RagState):
    chunks = state["chunks"]
    embeddings = model.encode(chunks, convert_to_tensor=False)
    return RagState({**state, "embeddings": embeddings})


def build_index_node(state: RagState):
    embeddings = np.array(state["embeddings"])

    dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    return RagState({**state, "index": index})


def retrieve_node(state: RagState):
    query = state["query"]
    query_vec = model.encode([query])
    index = state["index"]
    chunks = state["chunks"]
    _, I = index.search(np.array(query_vec), 5)
    retrieved = [chunks[i] for i in I[0]]
    return RagState({**state, "retrieved_chunks": retrieved})


def generate_node(state: RagState):
    context = "\n\n".join(state["retrieved_chunks"])
    query = state["query"]
    answer = generate_answer(context, query)
    return RagState({**state, "answer": answer})
