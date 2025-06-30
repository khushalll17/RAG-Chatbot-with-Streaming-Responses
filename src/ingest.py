import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from src.embedding import load_embedding_model
from src.cleaning import clean_text
from langchain.vectorstores import FAISS
from dotenv import load_dotenv
import os
import json

load_dotenv()

pdf_path = 'data/AI Training Document.pdf'
chunks_dir = 'chunks'
db_dir = 'vectordb'

loader = PyPDFLoader(pdf_path)
docs = loader.load()
for doc in docs:
    doc.page_content = clean_text(doc.page_content)

splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
chunks = splitter.split_documents(docs)

os.makedirs(chunks_dir, exist_ok=True)
# with open(os.path.join(chunks_dir, 'chunks.json'), 'w') as f:
#     json.dump([doc.page_content for doc in chunks], f)

chunk_data = [{"page_content": doc.page_content, "metadata": doc.metadata} for doc in chunks]

with open(os.path.join(chunks_dir, 'chunks.json'), 'w', encoding='utf-8') as f:
    json.dump(chunk_data, f, ensure_ascii=False, indent=2)

print(f"{len(chunks)} chunks created.")

embeddings = load_embedding_model()
vector_store = FAISS.from_documents(chunks, embeddings)
vector_store.save_local(db_dir)


print(f"Vector store saved at: {db_dir}")
