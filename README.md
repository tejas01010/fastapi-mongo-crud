# FastAPI MongoDB CRUD API

A simple CRUD (Create, Read, Update, Delete) REST API built using **FastAPI** and **MongoDB**.  
This project was developed to understand backend fundamentals such as API design, database integration, request validation, and error handling.

---

## 🚀 Features

- RESTful CRUD operations
- FastAPI framework with automatic Swagger UI
- MongoDB integration using PyMongo
- Pydantic models for request validation
- Proper HTTP status codes and error handling
- Clean and modular project structure

---

## 🧠 Tech Stack

- **Backend Framework**: FastAPI
- **Database**: MongoDB
- **Database Driver**: PyMongo
- **Validation**: Pydantic
- **Server**: Uvicorn

---

## 📂 Project Structure

fastapi-mongo-crud/
│
├── app/
│ ├── main.py # Application entry point
│ ├── routes.py # CRUD API endpoints
│ ├── models.py # Pydantic data models
│ └── database.py # MongoDB connection
│
├── requirements.txt
├── README.md
├── .env # Environment variables


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/tejas01010/fastapi-mongo-crud.git
cd fastapi-mongo-crud

---
   
2️⃣ Create and Activate Virtual Environment

python -m venv venv

venv\Scripts\activate


3️⃣ Install Dependencies
pip install -r requirements.txt


4️⃣ Configure Environment Variables

Create a .env file in the root directory:

MONGO_URL=your_mongodb_connection_string
DB_NAME=fastapi_db


5️⃣ Run the Application
uvicorn app.main:app --reload


The API will run at:

http://127.0.0.1:8000

📘 API Documentation (Swagger UI)

FastAPI automatically generates interactive API documentation.

Open in browser:

http://127.0.0.1:8000/docs