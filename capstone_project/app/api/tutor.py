from fastapi import APIRouter
from app.schemas.tutor import TutorRequest, TutorResponse
from app.core.persona import format_tutor_response
from app.core.llm import generate_answer
from app.core.rag import retrieve_context

router = APIRouter()


@router.post("/ask", response_model=TutorResponse)
def ask_tutor(request: TutorRequest):
    question = request.question.strip()

    # retrieve context + similarity distance
    context, distance = retrieve_context(question)

    # distance-based domain check
    if distance > 1.2:
        return TutorResponse(
            answer="This question does not relate to the history or philosophy topics I can help with.",
            in_domain=False
        )

    raw_answer = generate_answer(question, context)
    persona_answer = format_tutor_response(raw_answer)

    return TutorResponse(
        answer=persona_answer,
        in_domain=True
    )
