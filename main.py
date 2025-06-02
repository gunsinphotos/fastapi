from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Pydantic model
class Todo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

# In-memory database
todos: List[Todo] = []

# HTML UI
@app.get("/", response_class=HTMLResponse)
def serve_ui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# API endpoints
@app.post("/todos/", response_model=Todo)
def create_todo(todo: Todo):
    if any(t.id == todo.id for t in todos):
        raise HTTPException(status_code=400, detail="Todo with this ID already exists")
    todos.append(todo)
    return todo

@app.get("/todos/", response_model=List[Todo])
def get_todos():
    return todos

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for idx, todo in enumerate(todos):
        if todo.id == todo_id:
            del todos[idx]
            return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")
