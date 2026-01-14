from fastapi import FastAPI
from app.api.tutor import router as tutor_router

app = FastAPI(
    title="History / Philosophy Tutor",
    description="AI tutor with nuanced persona and tone",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(tutor_router, prefix="/tutor", tags=["Tutor"])
