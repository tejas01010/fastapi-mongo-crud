from groq import Groq
from app.core.config import GROQ_API_KEY, LLM_MODEL

client = Groq(api_key=GROQ_API_KEY)


def generate_answer(prompt: str, context: str) -> str:
    """
    Generate an answer using LLaMA with retrieved context (RAG).
    """

    system_prompt = (
        "You are a calm, patient academic tutor specializing in history and philosophy. "
        "You explain concepts step by step, adapting your tone to the student's needs. "
        "When a student seems curious, you expand gently. "
        "When a student seems confused, you simplify. "
        "When information is missing, you acknowledge limitations politely. "
        "Answer ONLY using the provided context."
    )


    user_prompt = f"""
Context:
{context}

Question:
{prompt}
"""

    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()
