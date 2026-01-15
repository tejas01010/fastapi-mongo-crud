from app.core.intent import detect_intent


def test_follow_up_intent():
    intent = detect_intent("Can you explain this more?")
    assert intent == "FOLLOW_UP"


def test_doubt_intent():
    intent = detect_intent("I didn't understand this")
    assert intent == "DOUBT"


def test_new_topic_intent():
    intent = detect_intent("What happened in World War 1?")
    assert intent == "NEW_TOPIC"
