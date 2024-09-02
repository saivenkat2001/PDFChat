from langchain_chroma import Chroma
from app.constants import persist_directory, embedding_function

class ChromaDBDemo:

    def __init__(self):
        '''
        Initializing chromadb
        '''
        self.persist_dir = persist_directory
        self.embedding_fun = embedding_function
        self.db = Chroma(persist_directory=self.persist_dir, embedding_function=self.embedding_fun)

    def add_vectors(self, documents):
        '''
        Method to add embeddings to vectordb
        '''
        vectorstore = self.db.from_documents(documents=documents, persist_directory=self.persist_dir, embedding=self.embedding_fun)
        return vectorstore

