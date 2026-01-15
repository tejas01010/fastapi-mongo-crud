import fitz  # PyMuPDF
import os

PDF_DIR = "data/pdfs"

def load_pdfs():
    documents = []

    for filename in os.listdir(PDF_DIR):
        if filename.endswith(".pdf"):
            path = os.path.join(PDF_DIR, filename)
            doc = fitz.open(path)

            full_text = ""
            for page in doc:
                full_text += page.get_text()

            documents.append({
                "source": filename,
                "text": full_text
            })

    return documents
