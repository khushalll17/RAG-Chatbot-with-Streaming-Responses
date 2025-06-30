import streamlit as st
from src.embedding import load_embedding_model
from src.retriever import get_retriever
from src.generator import load_llm
from src.rag_pipeline import build_chain
import json

st.set_page_config(page_title="RAG Chatbot", layout="wide")
st.title("Chat with AI Training Document")

try:
    with open("chunks/chunks.json", encoding="utf-8") as f:
        chunks_data = json.load(f)
        chunk_count = len(chunks_data)
except Exception as e:
    chunk_count = "Not Found"
    st.error(f"Error loading chunks: {e}")

with st.sidebar:
    st.markdown("### Model Info")
    st.write("Model: mistralai/Mistral-7B-Instruct-v0.3")
    st.write("Indexed Chunks: ", chunk_count)
    if st.button("Reset Chat"):
        st.session_state.history = []

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Ask a question:")

for pair in st.session_state.history:
    st.markdown(f"** You:** {pair['q']}")
    st.markdown(f"** Bot:** {pair['a']}")

if user_input:
    embedding_model = load_embedding_model()
    retriever = get_retriever("vectordb", embedding_model)
    llm = load_llm()
    chain = build_chain(retriever, llm)

    with st.spinner("Thinking..."):
        answer = chain.invoke(user_input)
        st.session_state.history.append({"q": user_input, "a": answer})
    st.experimental_set_query_params(dummy="1") 
    st.rerun() 