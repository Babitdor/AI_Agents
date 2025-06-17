import streamlit as st
from retriever import (
    RagState,
    parse_pdf_node,
    chunk_text_node,
    embed_node,
    build_index_node,
    retrieve_node,
    generate_node,
)

from langgraph.graph import StateGraph, START, END
from langchain_core.runnables import RunnableLambda

st.set_page_config(layout="wide")
st.title("🧠 Talking to a PDF?? Are you Crazy?")

uploaded_pdf = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_pdf:
    question = st.text_input("Ask a question about your notes")

    if question:
        with st.spinner("Running Agents...."):

            graph = StateGraph(RagState)
            graph.add_node("parse_node", parse_pdf_node)
            graph.add_node("chunks_node", chunk_text_node)
            graph.add_node("embed_node", embed_node)
            graph.add_node("index_node", build_index_node)
            graph.add_node("retrieve_node", retrieve_node)
            graph.add_node("answer_node", generate_node)

            graph.add_edge(START, "parse_node")
            graph.add_edge("parse_node", "chunks_node")
            graph.add_edge("chunks_node", "embed_node")
            graph.add_edge("embed_node", "index_node")
            graph.add_edge("index_node", "retrieve_node")
            graph.add_edge("retrieve_node", "answer_node")
            graph.add_edge("answer_node", END)

            rag_chain = graph.compile()

            final_state = rag_chain.invoke({"file": uploaded_pdf, "query": question})

        st.success("Answer Generated!")
        st.markdown(f"Answer :: {final_state['answer']}")
