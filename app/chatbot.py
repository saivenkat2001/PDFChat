from app.constants import embedding_function, persist_directory
from langchain.chains import create_retrieval_chain
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.memory import ConversationBufferMemory
from langchain.prompts.chat import ChatPromptTemplate
from app.llms.google_gen_AI import GoogleLLM
from app.vectordb.chromadb import ChromaDBDemo

class ChatBot:
    def __init__(self):
        self.embedding_function = embedding_function
        self.persist_directory = persist_directory
        self.chat_history = []
    
    def answer_query(self, message, chat_history):
        llm = GoogleLLM().llm
        vectorstore = ChromaDBDemo().db
        retriever = vectorstore.as_retriever()

        system_prompt = (
            "Use the given context to answer the question. "
            "If you don't know the answer, say you don't know. "
            "Use three sentences maximum and keep the answer concise. "
            "Context: {context}"
        )
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{input}"),
        ])
        question_answer_chain = create_stuff_documents_chain(llm, prompt)
        chain = create_retrieval_chain(retriever, question_answer_chain)

        memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True, output_key='result')

        qa_chain = RetrievalQA.from_llm(
            llm=llm,
            retriever=retriever,
            memory=memory,
            return_source_documents=True
        )

        response = qa_chain.invoke({"query": message})
        chat_history.append((message, response['result']))
        return "", chat_history
