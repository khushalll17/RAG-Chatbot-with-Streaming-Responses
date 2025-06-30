from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

def load_llm():
    model = HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct-v0.3",
        task="text-generation",
        streaming=True,
        model_kwargs={"device": "cpu"}
    )
    return ChatHuggingFace(llm=model)