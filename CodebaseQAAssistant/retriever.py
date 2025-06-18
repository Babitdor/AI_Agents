from langgraph.graph import StateGraph, END, START
from typing import TypedDict, List, Optional
import faiss
from tools import (
    clone_repo,
    extract_code_chunks,
    embed_chunks,
    retrieve_chunks,
    generate_answer,
)


class CodeAgentState(TypedDict):
    url: str
    repo_path: str
    chunks: List[str]
    index: Optional[faiss.IndexFlatL2]
    embeddings: Optional[List[List[float]]]
    query: str
    retrieved_chunks: List[str]  # Think of this as the context
    answer: Optional[str]


def clone_repo_node(state: CodeAgentState):
    repo_path = clone_repo(state["url"])
    return CodeAgentState({**state, "repo_path": repo_path})


def parse_node(state: CodeAgentState):
    chunks = extract_code_chunks(state["repo_path"])
    return CodeAgentState({**state, "chunks": chunks})


def embed_node(state: CodeAgentState):
    index, chunks, embeddings = embed_chunks(state["chunks"])
    return CodeAgentState({**state, "index": index, "embeddings": embeddings})


def retrieve_node(state: CodeAgentState):
    matches = retrieve_chunks(state["query"], state["chunks"], state["embeddings"])
    return CodeAgentState({**state, "retrieved_chunks": "\n\n".join(matches)})


def answer_node(state: CodeAgentState):
    answer = generate_answer(state["retrieved_chunks"], state["query"])
    return CodeAgentState({**state, "answer": answer})


graph = StateGraph(CodeAgentState)

# Nodes
graph.add_node("clone", clone_repo_node)
graph.add_node("parse", parse_node)
graph.add_node("embed", embed_node)
graph.add_node("retrieve", retrieve_node)
graph.add_node("generate_answer", answer_node)

# Edges
graph.add_edge(START, "clone")
graph.add_edge("clone", "parse")
graph.add_edge("parse", "embed")
graph.add_edge("embed", "retrieve")
graph.add_edge("retrieve", "generate_answer")
graph.add_edge("generate_answer", END)

rag_chain = graph.compile()
