from fastapi import FastAPI
from app.routes.vector_routes import router as vector_router

app = FastAPI(title="AI Vector Search API")

app.include_router(vector_router)
