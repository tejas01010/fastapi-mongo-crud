from app.core.rag import load_documents

def test_load_documents_returns_list():
    docs = load_documents()
    assert isinstance(docs, list)
    assert len(docs) > 0
