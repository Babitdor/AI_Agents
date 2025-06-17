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

if "messages" not in st.session_state:
    st.session_state.messages = []

uploaded_pdf = st.file_uploader("Upload a PDF", type="pdf")


@st.cache_resource(show_spinner=False)
def build_rag_chain():
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
    return graph.compile()


# Load RAG pipeline
rag_chain = build_rag_chain()

# Display chat history
if st.session_state.messages:
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# Input area
if uploaded_pdf:
    user_input = st.chat_input("Ask a question about your PDF")

    if user_input:
        # Display user message
        st.chat_message("user").markdown(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Run LangGraph
        with st.spinner("Thinking..."):
            final_state = rag_chain.invoke({"file": uploaded_pdf, "query": user_input})

        # Display assistant message
        assistant_response = final_state["answer"]
        st.chat_message("assistant").markdown(assistant_response)
        st.session_state.messages.append(
            {"role": "assistant", "content": assistant_response}
        )
