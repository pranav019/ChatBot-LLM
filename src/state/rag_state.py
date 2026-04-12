from typing import List
from pydantic import BaseModel
from langchain.schema import Document


class RAGState(BaseModel):
    question: str
    retrived_docs = List[Document] = []

    answer: str = ""

    # from typing import List
    # from pydantic import BaseModel, Field
    # from langchain_core.documents import Document

    # class RAGState(BaseModel):
    #     question: str
    #     retrieved_docs: List[Document] = Field(default_factory=list)
    #     answer: str = ""

    """    FLOW :-
            Initial State:
            ----------------
            question = "What is AI?"
            retrieved_docs = []
            answer = ""

                    ↓

            After Retriever Node:
            ----------------
            question = "What is AI?"
            retrieved_docs = [doc1, doc2]
            answer = ""

                    ↓

            After LLM Node:
            ----------------
            question = "What is AI?"
            retrieved_docs = [doc1, doc2]
            answer = "AI is..."
    """
