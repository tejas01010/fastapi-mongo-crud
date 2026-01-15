from fastapi import APIRouter
from app.schemas.tutor import TutorRequest, TutorResponse
from app.core.rag import retrieve_context
from app.core.llm import generate_answer
from app.core.persona import format_tutor_response
from app.core.intent import detect_intent
from app.core.follow_up import needs_resolution, resolve_followup

router = APIRouter()
conversation_memory = {}


@router.post("/ask", response_model=TutorResponse)
def ask_tutor(request: TutorRequest):
    question = request.question.strip()
    convo_id = request.conversation_id
    intent = detect_intent(question)

    # -------------------------------
    # FOLLOW-UP RESOLUTION
    # -------------------------------
    if convo_id and convo_id in conversation_memory:
        memory = conversation_memory[convo_id]
        entity = memory.get("entity")

        if entity and needs_resolution(question):
            question = resolve_followup(question, entity)

    # -------------------------------
    # RETRIEVAL
    # -------------------------------
    context, distance = retrieve_context(question)

    if distance > 1.2:
        return TutorResponse(
            answer="This question does not relate to the history or philosophy topics I can help with.",
            in_domain=False
        )

    raw_answer = generate_answer(question, context)
    final_answer = format_tutor_response(raw_answer)

    # -------------------------------
    # MEMORY UPDATE
    # -------------------------------
    if convo_id:
        # crude but effective entity extraction for now
        if "socrates" in question.lower():
            entity = "Socrates"
        elif "plato" in question.lower():
            entity = "Plato"
        else:
            entity = conversation_memory.get(convo_id, {}).get("entity")

        conversation_memory[convo_id] = {
            "entity": entity,
            "context": context,
            "topic": question
        }

    return TutorResponse(answer=final_answer, in_domain=True)
