from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    task: str
    completed: bool = False

@app.get('/todos', response_model=List[Todo])
def get_todos():
    return todos

@app.post('/todos', response_model=Todo)
def create_todo(todo: Todo):
    todos.append(todo)
    return todo

@app.delete('/todos/{todo_id}')
def delete_todo(todo_id: int):
    global todos
    todos = [todo for todo in todos if todo.id != todo_id]
    return {'message': 'Todo deleted'}
