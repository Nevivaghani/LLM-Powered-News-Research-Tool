import os
os.environ["STREAMLIT_FILE_WATCHER_TYPE"] = "none"


import streamlit as st
from langchain_helper import create_vector_db, get_qa_chain

st.title("Codebasics QA")
btn = st.button("Create Knowledge Base")

if btn:
    create_vector_db()
    st.success("✅ Vector DB created and saved successfully!")

question = st.text_input("Question:")

if question:
    if not os.path.exists("faiss_index/index.faiss"):
        st.error("⚠️ Knowledge base not found. Please click the button above to create it.")
    else:
        chain = get_qa_chain()
        response = chain(question)
        st.header("Answer:")
        st.write(response["result"])
