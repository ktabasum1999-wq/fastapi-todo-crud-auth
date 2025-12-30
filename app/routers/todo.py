from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Todo
from ..schemas import TodoCreate, TodoResponse

router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Todo
@router.post("/", response_model=TodoResponse)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    new_todo = Todo(
        title=todo.title,
        description=todo.description
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

# Read all Todos
@router.get("/", response_model=list[TodoResponse])
def get_all_todos(db: Session = Depends(get_db)):
    return db.query(Todo).all()

# Delete Todo
@router.delete("/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(todo)
    db.commit()
    return {"message": "Todo deleted successfully"}
