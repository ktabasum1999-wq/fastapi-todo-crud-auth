from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

app = FastAPI()

# Authentication setup
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Dummy user data
users = {
    "admin": "admin123"
}

# Dummy token
TOKEN = "my-secret-token"

# In-memory todo storage
todos = []

# Todo model
class Todo(BaseModel):
    title: str
    completed: bool = False

# LOGIN (Authentication)
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if users.get(form_data.username) != form_data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
    return {
        "access_token": TOKEN,
        "token_type": "bearer"
    }

# Authorization check
def get_current_user(token: str = Depends(oauth2_scheme)):
    if token != TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized"
        )
    return token

# CREATE todo
@app.post("/todos")
def create_todo(todo: Todo, user=Depends(get_current_user)):
    todos.append(todo)
    return {"message": "Todo created", "todo": todo}

# READ todos
@app.get("/todos")
def read_todos(user=Depends(get_current_user)):
    return todos

# UPDATE todo
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: Todo, user=Depends(get_current_user)):
    if todo_id >= len(todos):
        raise HTTPException(status_code=404, detail="Todo not found")
    todos[todo_id] = todo
    return {"message": "Todo updated", "todo": todo}

# DELETE todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, user=Depends(get_current_user)):
    if todo_id >= len(todos):
        raise HTTPException(status_code=404, detail="Todo not found")
    todos.pop(todo_id)
    return {"message": "Todo deleted"}
