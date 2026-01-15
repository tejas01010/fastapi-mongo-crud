from app.core.rag import retrieve_context


def test_retrieve_context_returns_text():
    context, distance = retrieve_context("Who was Socrates?")
    assert isinstance(context, str)
    assert len(context) > 0
    assert isinstance(distance, float)
