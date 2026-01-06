from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    name: str
    email: str
    age: int
