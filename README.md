# FastAPI Todo CRUD App

A simple and clean **Todo CRUD REST API** built using **FastAPI**, **SQLAlchemy**, and **SQLite**.  
This project demonstrates backend fundamentals including API design, database integration, and request/response validation.


## 🚀 Features

- Create, Read, and Delete Todos
- FastAPI automatic Swagger documentation
- SQLite database with SQLAlchemy ORM
- Clean project structure (industry-style)
- Pydantic schemas for validation
- Persistent data storage


## 🛠 Tech Stack

- **Python 3.13**
- **FastAPI**
- **SQLAlchemy**
- **SQLite**
- **Uvicorn**


## 📂 Project Structure
fastAPI-todo-app/
│
├── app/
│ ├── init.py
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── schemas.py
│ └── routers/
│ ├── init.py
│ └── todo.py
│
├── todo.db
├── requirements.txt
└── README.md


## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

git clone https://github.com/ktabasum1999-wq/fastapi-todo-crud-auth.git
cd fastapi-todo-crud-auth
Install dependencies
pip install fastapi uvicorn sqlalchemy
Run the application
python -m uvicorn app.main:app --reload

API Documentation (Swagger)

After running the server, open your browser:

http://127.0.0.1:8000/docs
API Endpoints
➕ Create Todo

POST /todos

{
  "title": "Learn FastAPI",
  "description": "CRUD project for interview"
}

📄 Get All Todos
GET /todos

❌ Delete Todo

DELETE /todos/{todo_id}

✅ Sample Response
{
  "id": 1,
  "title": "Learn FastAPI",
  "description": "CRUD project for interview",
  "completed": false
}
Author

Tabasum Khan
Aspiring Backend / AI Engineer
GitHub: https://github.com/ktabasum1999-wq

