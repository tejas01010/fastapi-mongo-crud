import re

def normalize(text: str) -> str:
    return re.sub(r"[^\w\s]", "", text.lower().strip())


def detect_intent(text: str) -> str:
    text = normalize(text)

    follow_up_phrases = [
        "explain more",
        "tell me more",
        "go deeper",
        "continue",
        "what about this",
        "can you explain this",
        "more detail",
    ]

    doubt_phrases = [
        "i dont understand",
        "i didnt understand",
        "i did not understand",
        "confused",
        "clarify",
        "can you repeat",
        "explain again",
        "not clear"
    ]

    social_phrases = [
        "good morning",
        "good evening",
        "hello",
        "hi ",
        "thanks",
        "thank you"
    ]

    # 1️⃣ FOLLOW-UP
    if any(p in text for p in follow_up_phrases):
        return "FOLLOW_UP"

    # 2️⃣ DOUBT
    if any(p in text for p in doubt_phrases):
        return "DOUBT"

    # 3️⃣ SOCIAL
    if any(p in text for p in social_phrases):
        return "SOCIAL"

    # 4️⃣ DEFAULT
    return "NEW_TOPIC"
