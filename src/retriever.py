from langchain.vectorstores import FAISS

def get_retriever(db_path, embedding_model):
    vector_store = FAISS.load_local(db_path, embedding_model, allow_dangerous_deserialization=True)
    return vector_store.as_retriever(search_type="similarity",search_kwargs={"k": 4})