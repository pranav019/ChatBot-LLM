from typing import List
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.schema import Document


class VectorStore:
    "Manages vector store application"

    def __init__(self):
        self.embedding = OpenAIEmbeddings()
        self.vectorstore = None
        self.retriever = None

    def create_retriever(self, documents: List[Document]):

        self.vectorstore = FAISS.from_document(documents, self.embedding)
        self.retriever = self.vectorstore.as_retriever()

    def get_retriever(self):
        if self.retriever is None:
            raise ValueError(
                "Vector Store not initialized, call create_vectorstore first."
            )
        return self.retriever

    def retrieve(self, query: str, k: int = 4) -> List[Document]:
        if self.retriever is None:
            raise ValueError(
                "Vector Store not initialized, call create_vectorstore first."
            )
        return self.retriever.invoke(query)
    
