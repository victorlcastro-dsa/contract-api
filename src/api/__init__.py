from quart import Quart #,request, jsonify
# from quart_schema import QuartSchema, validate_request, validate_response
# from pydantic import BaseModel
# from datetime import datetime
from src.api.database import init_db, close_db

app = Quart(__name__)
app.config["DEBUG"] = True  # Enable debug mode
# QuartSchema(app)

# class TodoIn(BaseModel):
#     task: str
#     due: datetime | None

# class TodoIn(BaseModel):
#     task: str
#     due: datetime | None

# class Todo(TodoIn):
#     id: int

@app.before_serving
async def startup():
    await init_db()

@app.after_serving
async def shutdown():
    await close_db()

# @app.post("/todos/")
# @validate_request(TodoIn)
# @validate_response(Todo)
# async def create_todo(data: TodoIn) -> Todo:
#     return Todo(id=1, task=data.task, due=data.due)

# @app.post("/echo")
# async def echo():
#     data = await request.get_json()
#     return jsonify({"extra": True, "input": data})

def run() -> None:
    app.run(host="0.0.0.0")