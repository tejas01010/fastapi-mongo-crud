from fastapi import APIRouter, UploadFile, File
from app.services.document_loader import read_pdf, read_txt
from app.services.vector_service import create_vectors_from_document
import tempfile
import os

router = APIRouter(prefix="/vectors", tags=["Vectors"])


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    suffix = os.path.splitext(file.filename)[1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    if suffix == ".pdf":
        text = read_pdf(tmp_path)
    elif suffix == ".txt":
        text = read_txt(tmp_path)
    else:
        return {"error": "Unsupported file type"}

    os.remove(tmp_path)

    return create_vectors_from_document(text)

from app.schemas import VectorSearchRequest, VectorSearchResponse
from app.services.vector_service import search_vectors


@router.post("/search", response_model=VectorSearchResponse)
def search_documents(request: VectorSearchRequest):
    results = search_vectors(request.query, request.top_k)

    return {
        "matched": len(results) > 0,
        "results": results
    }

