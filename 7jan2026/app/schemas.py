from pydantic import BaseModel
from typing import List





class VectorSearchRequest(BaseModel):
    query: str
    top_k: int = 3


class SearchResult(BaseModel):
    document: str
    distance: float


class VectorSearchResponse(BaseModel):
    matched: bool
    results: List[SearchResult]
