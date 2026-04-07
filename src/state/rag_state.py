from typing import List
from pydantic import BaseModel
from langchain.schema import Document


class RAGState(BaseModel):
    question: str
    retrived_docs = List[Document] = []
    answer: str = ""
