from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
persist_directory = "output/cat"
google_llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", temperature=0.7)