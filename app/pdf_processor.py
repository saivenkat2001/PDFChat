from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from app.constants import embedding_function
from app.vectordb.chromadb import ChromaDBDemo

class PDFProcessor:
    def __init__(self):
        self.embedding_function = embedding_function

    def add_docs(self, path):
        pdf_reader = PdfReader(path)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=100,
            length_function=len
        )
        chunks = text_splitter.split_text(text)
        documents = [Document(page_content=chunk) for chunk in chunks]

        db = ChromaDBDemo()
        return db.add_vectors(documents=documents) 