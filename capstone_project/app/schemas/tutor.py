from pydantic import BaseModel
from typing import Optional

class TutorRequest(BaseModel):
    question: str
    conversation_id: Optional[str] = None


class TutorResponse(BaseModel):
    answer: str
    in_domain: bool
