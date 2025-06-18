# app.py
import streamlit as st
from retriever import rag_chain

st.set_page_config(layout="wide")
st.title("🤖 Codebase QA Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

repo_url = st.text_input("🔗 Enter GitHub Repo URL:")

if repo_url:
    user_query = st.chat_input("Ask something about the code...")

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if user_query:
        st.chat_message("user").markdown(user_query)
        st.session_state.messages.append({"role": "user", "content": user_query})

        with st.spinner("Analyzing code..."):
            final_state = rag_chain.invoke({"url": repo_url, "query": user_query})

        response = final_state["answer"]
        st.chat_message("assistant").markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
