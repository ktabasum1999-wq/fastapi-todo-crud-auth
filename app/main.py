from fastapi import FastAPI
from .database import Base, engine
from .routers import todo

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Todo CRUD App")

# Include routers
app.include_router(todo.router)

@app.get("/")
def root():
    return {"message": "FastAPI Todo App is running 🚀"}
