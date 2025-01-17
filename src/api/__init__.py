from quart import Quart
from .database import Database
from quart_bcrypt import Bcrypt

app = Quart(__name__)
app.config["DEBUG"] = True  # Enable debug mode
app.config["BCRYPT_LOG_ROUNDS"] = 12  # Security configuration for Bcrypt

bcrypt = Bcrypt(app)
database = Database()

@app.before_serving
async def startup():
    await database.init_db()

@app.after_serving
async def shutdown():
    await database.close_db()

def run() -> None:
    app.run(host="0.0.0.0")

#,request, jsonify
# from quart_schema import QuartSchema, validate_request, validate_response
# from pydantic import BaseModel
# from datetime import datetime
# QuartSchema(app)

# class TodoIn(BaseModel):
#     task: str
#     due: datetime | None

# class TodoIn(BaseModel):
#     task: str
#     due: datetime | None

# class Todo(TodoIn):
#     id: int

# @app.post("/todos/")
# @validate_request(TodoIn)
# @validate_response(Todo)
# async def create_todo(data: TodoIn) -> Todo:
#     return Todo(id=1, task=data.task, due=data.due)

# @app.post("/echo")
# async def echo():
#     data = await request.get_json()
#     return jsonify({"extra": True, "input": data})
