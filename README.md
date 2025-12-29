# FastAPI To-Do Application (CRUD with Authentication & Authorization)

This repository contains a **FastAPI-based To-Do application** developed as a technical task.  
The project demonstrates **CRUD operations**, **authentication**, and **authorization** using FastAPI.


## 🚀 Features

- User Authentication (Login)
- Token-based Authorization
- CRUD Operations:
  - Create To-Do
  - Read To-Dos
  - Update To-Do
  - Delete To-Do
- FastAPI with Swagger UI
- Input validation using Pydantic
- In-memory data storage (no database)
- No Machine Learning models used

## 🛠️ Tech Stack
- Python 3
- FastAPI
- Uvicorn
- Pydantic

## 📂 Project Structure
  fastapi-todo-crud-auth/
│
├── main.py
└── README.md



## ▶️ How to Run the Project

### 1. Clone the repository

git clone https://github.com/ktabasum1999-wq/fastapi-todo-crud-auth.git
cd fastapi-todo-crud-auth

Install dependencies
python -m pip install fastapi uvicorn python-multipart
3. Run the application
bash
Copy code
python -m uvicorn main:app --reload
API Documentation

After running the server, open the following URL in your browser:

http://127.0.0.1:8000/docs


This opens the Swagger UI where all endpoints can be tested.

 Authentication & Authorization
Login Credentials (for testing)

Username: admin

Password: admin123

Steps:

Use POST /login to authenticate

Copy the access token

Click Authorize in Swagger UI
Paste:

Bearer my-secret-token


Access all CRUD endpoints
API Endpoints
Method	Endpoint	Description
POST	/login	User login
POST	/todos	Create a todo
GET	/todos	Get all todos
PUT	/todos/{todo_id}	Update a todo
DELETE	/todos/{todo_id}	Delete a todo

(All /todos endpoints require authorization)
Notes

This project focuses purely on backend logic and API design

No frontend and no database are used

Data is stored in memory for simplicity

 Author

TABASUM Khan
Python / FastAPI Developer




