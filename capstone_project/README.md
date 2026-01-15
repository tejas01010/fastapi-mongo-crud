# History / Philosophy Tutor Capstone 

# 📚 Conversational AI Tutor (History & Philosophy)

A **conversational AI tutor** built using **FastAPI, FAISS, Sentence Transformers, and LLaMA (via Groq)**.  
The system answers **history and philosophy related questions** using a **Retrieval-Augmented Generation (RAG)** approach and supports **human-like conversational flow**, similar to ChatGPT.

This project is designed as a **capstone-level application** focusing on:
- Vector databases
- Custom prompting
- Nuanced tutor persona
- Conversational memory
- Testing & coverage

---

## ✨ What This Project Does

### ✅ Core Functionality
- Answers questions **only from a provided knowledge base**
- Maintains **context-aware conversation** (follow-up questions, doubts)
- Rejects **out-of-domain queries** politely (e.g., DSA, coding, casual chat)
- Responds in a **calm, academic tutor tone**

### ✅ Knowledge Handling
- Reads knowledge from:
  - `.txt` files
  - `.pdf` files
- Splits content into **overlapping chunks**
- Generates embeddings using **Sentence Transformers**
- Stores vectors in **FAISS Vector Database**

### ✅ Intelligence Layer (RAG)
- Retrieves the most relevant chunks using semantic similarity
- Uses **LLaMA (Groq API)** to generate grounded answers
- Ensures answers stay within retrieved context

### ✅ Conversational Behavior
- Detects user intent:
  - New topic
  - Follow-up
  - Doubt / clarification
  - Social greeting
- Remembers topic context using `conversation_id`
- Responds like a **human tutor**, not a chatbot

### ✅ Engineering Practices
- Modular backend architecture
- Pytest-based unit testing
- Code coverage report generated

---

## 🧠 High-Level Architecture

User Question
↓
Intent Detection
↓
Vector Search (FAISS)
↓
Relevant Context (Chunks)
↓
LLaMA (Groq API)
↓
Tutor Persona Formatting
↓
Final Answer


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd capstone_project

2️⃣ Create Virtual Environment
py -3.10 -m venv venv


Activate it:

Windows

venv\Scripts\activate


3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set Environment Variables

Create a .env file in the root directory:

GROQ_API_KEY=your_groq_api_key_here


⚠️ Do not commit .env to GitHub.

📚 Preparing the Knowledge Base
Add Knowledge Files

Place .txt files in:

data/corpus/


Place .pdf files in:

data/pdfs/

Build the Vector Store
python -c "from app.core.rag import build_vector_store; build_vector_store()"


You should see output like:

✅ FAISS index built with XX chunks

▶️ Running the Application

Start the FastAPI server:

uvicorn app.main:app --reload


Open Swagger UI in browser:

http://127.0.0.1:8000/docs

OR Streamlit UI:

streamlit run streamlit_app.py