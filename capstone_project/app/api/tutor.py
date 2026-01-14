from fastapi import APIRouter
from app.schemas.tutor import TutorRequest, TutorResponse
from app.core.persona import format_tutor_response

router = APIRouter()


@router.post("/ask", response_model=TutorResponse)
def ask_tutor(request: TutorRequest):
    question = request.question.lower()

    history_keywords = ["history", "philosophy", "philosopher", "ancient", "war"]

    in_domain = any(keyword in question for keyword in history_keywords)

    if not in_domain:
        return TutorResponse(
            answer="This question does not fall under history or philosophy. Please ask something related to those subjects.",
            in_domain=False
        )

    base_answer = (
        "This is an important idea in history and philosophy. "
        "Rather than memorizing definitions, it is useful to understand the context in which such ideas emerged."
    )

    persona_answer = format_tutor_response(base_answer)

    return TutorResponse(
        answer=persona_answer,
        in_domain=True
    )
