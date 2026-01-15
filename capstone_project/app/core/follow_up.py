import re

PRONOUNS = {"they", "them", "their", "he", "him", "his", "this", "that"}


def needs_resolution(question: str) -> bool:
    tokens = set(re.findall(r"\b\w+\b", question.lower()))
    return bool(tokens & PRONOUNS)


def resolve_followup(question: str, entity: str) -> str:
    return f"{question} (in reference to {entity})"
