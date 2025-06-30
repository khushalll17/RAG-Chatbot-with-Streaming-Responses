# RAG-Chatbot-with-Streaming-Responses
This project is an end-to-end Retrieval-Augmented Generation (RAG) chatbot built using LangChain, Hugging Face models, FAISS, and Streamlit. It allows users to query a PDF document (e.g., training material) and get contextual answers in real time, with a ChatGPT-like typing effect.

# Project Architecture
/data         - Raw PDF documents
/chunks       - Processed and chunked text
/vectordb     - Vector DB built using FAISS
/src          - Core backend modules
  ├─ cleaning.py       - Cleans and preprocesses PDF text
  ├─ embedding.py      - Loads sentence transformer embeddings
  ├─ retriever.py      - Loads FAISS and creates retriever
  ├─ generator.py      - Loads HuggingFace LLM
  ├─ rag_pipeline.py   - Builds prompt + RAG pipeline
  └─ stream_handler.py - Custom Streamlit-compatible stream output

app.py        - Streamlit UI with streaming support
notebooks/    - Jupyter testing & dev notebooks
requirements.txt - Python dependencies

# Preprocessing & Pipeline Setup
## Step 1: Prepare the document
Put your PDF inside the /data folder.

## Step 2: Ingest and preprocess
python -m src.ingest
This: Loads and cleans the PDF using BeautifulSoup Chunks it using NLTK (sentence-aware) Generates embeddings using all-MiniLM-L6-v2 Saves to FAISS vector DB under /vectordb

## Step 3: Run chatbot with RAG pipeline
streamlit run app.py

# Model Choices
## Embeddings
sentence-transformers/all-MiniLM-L6-v2
Loaded using LangChain + sentence-transformers device="cpu" enforced to avoid PyTorch meta tensor errors

## LLM
mistralai/Mistral-7B-Instruct-v0.3
Loaded using HuggingFaceEndpoint streaming=True with custom Streamlit callback for token-by-token output

## Chatbot with Streaming Responses
The chatbot uses a custom StreamHandler to display output as the model generates tokens Streaming is enabled via streaming=True and a placeholder st.empty() for live markdown updates

# Demo Video
link = https://drive.google.com/file/d/1YzcJhLnmLwj1sqX7txceyrTKv4HKny_-/view?usp=sharing
