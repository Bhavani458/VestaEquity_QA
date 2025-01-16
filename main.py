
import streamlit as st
from langchain_helper import get_qa_chain, create_vector_db

st.title("Vesta Equity Q&A 🏠")
st.header("Process all FAQs by clicking the below button:")
btn = st.button("Process FAQs")
if btn:
    create_vector_db()

question = st.text_input("Question: ")

if question:
    chain = get_qa_chain()
    response = chain(question)

    st.header("Answer")
    st.write(response["result"])
