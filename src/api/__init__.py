from dataclasses import dataclass
from datetime import datetime
from quart import Quart, request, jsonify
from quart_schema import QuartSchema, validate_request, validate_response
from pydantic import BaseModel

app = Quart(__name__)
app.config["DEBUG"] = True  # Enable debug mode
QuartSchema(app)

class TodoIn(BaseModel):
    task: str
    due: datetime | None

class TodoIn(BaseModel):
    task: str
    due: datetime | None

class Todo(TodoIn):
    id: int

@app.post("/todos/")
@validate_request(TodoIn)
@validate_response(Todo)
async def create_todo(data: TodoIn) -> Todo:
    return Todo(id=1, task=data.task, due=data.due)

@app.post("/echo")
async def echo():
    data = await request.get_json()
    return jsonify({"extra": True, "input": data})

def run() -> None:
    app.run()