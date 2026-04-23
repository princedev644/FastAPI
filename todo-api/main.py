from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root API
@app.get("/")
def read_root():
    return {"message": "To-Do API with PostgreSQL is running"}

# Get all todos
@app.get("/todos")
def get_todos(db: Session = Depends(get_db)):
    return db.query(models.Todo).all()

# Add todo
@app.post("/todos")
def add_todo(item: str, db: Session = Depends(get_db)):
    new_todo = models.Todo(task=item)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

# Delete todo
@app.delete("/todos/{id}")
def delete_todo(id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(todo)
    db.commit()
    return {"message": "Deleted successfully"}

# Update todo
@app.put("/todos/{id}")
def update_todo(id: int, new_item: str, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    todo.task = new_item
    db.commit()
    db.refresh(todo)
    return todo