# RAG-Chatbot-with-Streaming-Responses

This project is an end-to-end Retrieval-Augmented Generation (RAG) chatbot built using LangChain, Hugging Face models, FAISS, and Streamlit. It allows users to query a PDF document (e.g., training material) and get contextual answers in real time, with a ChatGPT-like typing effect.

# Project Architecture

/data         - Raw PDF documents

/chunks       - Processed and chunked text

/vectordb     - Vector DB built using FAISS

/src          - Core backend modules

  cleaning.py       - Cleans and preprocesses PDF text
  
  embedding.py      - Loads sentence transformer embeddings
  
  retriever.py      - Loads FAISS and creates retriever
  
  generator.py      - Loads HuggingFace LLM
  
  rag_pipeline.py   - Builds prompt + RAG pipeline
  
  stream_handler.py - Custom Streamlit-compatible stream output

app.py        - Streamlit UI with streaming support

notebooks/    - Jupyter testing & dev notebooks

requirements.txt - Python dependencies

# Preprocessing & Pipeline Setup

## Step 1: Prepare the document

Place your PDF file inside the /data folder. Before processing, ensure the document is clean and well-formatted. This may involve removing unwanted headers, footers,
repeated page numbers, or embedded HTML tags. The cleaning.py module is designed to help strip such noise from the text so that chunking and embedding produce meaningful
segments. A well-prepared document improves the quality of retrieved answers and reduces irrelevant or noisy output from the chatbot.

## Step 2: Ingest and preprocess

python -m src.ingest

This script performs the complete document ingestion workflow. It loads the PDF from the /data folder and cleans the content using BeautifulSoup and custom logic to remove
unnecessary formatting, headers, or HTML tags. The cleaned text is then split into meaningful 100–300 word segments using sentence-aware splitting via
RecursiveCharacterTextSplitter. After chunking, semantic embeddings are generated using a pre-trained model sentence-transformers/all-MiniLM-L6-v2. Finally, the embeddings
are stored in a FAISS vector database inside the /vectordb directory to enable fast semantic search during retrieval.


## Step 3: Run chatbot with RAG pipeline

Once embeddings have been created and stored, launch the chatbot by running the Streamlit interface. The application loads the vector database and uses a retriever to fetch
semantically relevant chunks based on the user's question. These retrieved chunks, along with the user's input, are passed through a custom RAG pipeline composed of a prompt
template, a language model mistralai/Mistral-7B-Instruct-v0.3, and an output parser. The chatbot displays real-time responses, including previously asked questions and
answers, while streaming the model's output token-by-token using a custom callback handler. This step completes the end-to-end document-based question-answering workflow
with live interaction and dynamic context grounding.

# Model Choices

## Embeddings
sentence-transformers/all-MiniLM-L6-v2
Loaded using LangChain + sentence-transformers device="cpu" enforced to avoid PyTorch meta tensor errors

## LLM
mistralai/Mistral-7B-Instruct-v0.3
Loaded using HuggingFaceEndpoint streaming=True with custom Streamlit callback for token-by-token output

## Chatbot with Streaming Responses

The chatbot delivers a real-time, conversational experience by using a custom StreamHandler that streams the model's output token-by-token as it is generated. This is
achieved by enabling streaming=True when loading the LLM and using a dynamic placeholder (st.empty()) in the Streamlit interface to update the UI incrementally. As a result,
responses appear as if the bot is “typing” live, improving interactivity and reducing perceived latency.

# Demo Video
link = https://drive.google.com/file/d/1YzcJhLnmLwj1sqX7txceyrTKv4HKny_-/view?usp=sharing
