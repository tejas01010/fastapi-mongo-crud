from fastapi import APIRouter
from app.schemas import (
    VectorCreateRequest,
    VectorSearchRequest,
    VectorSearchResponse
)
from app.services.vector_service import create_vector, search_vectors

router = APIRouter(prefix="/vectors", tags=["Vectors"])


@router.post("")
def create_vector_endpoint(request: VectorCreateRequest):
    return create_vector(request.text)


@router.post("/search", response_model=VectorSearchResponse)
def search_vectors_endpoint(request: VectorSearchRequest):
    results = search_vectors(request.query, request.top_k)

    return {
        "matched": len(results) > 0,
        "results": results
    }
