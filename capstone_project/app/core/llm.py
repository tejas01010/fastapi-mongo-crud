from groq import Groq
from app.core.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def generate_answer(prompt: str, context: str) -> str:
    """
    Generate an answer using LLaMA with retrieved context (RAG).
    """

    system_prompt = (
        "You are a calm academic tutor specializing in history and philosophy. "
        "Answer ONLY using the provided context. "
        "If the context is insufficient, say you cannot answer."
    )

    user_prompt = f"""
Context:
{context}

Question:
{prompt}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()
