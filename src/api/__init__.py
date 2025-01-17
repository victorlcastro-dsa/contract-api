from quart import Quart, request, jsonify
from quart_schema import QuartSchema, validate_request, validate_response
from .database import Database
from quart_bcrypt import Bcrypt
from .schemas import ContactSchema

app = Quart(__name__)
app.config["DEBUG"] = True  # Enable debug mode
app.config["BCRYPT_LOG_ROUNDS"] = 12  # Security configuration for Bcrypt

bcrypt = Bcrypt(app)
database = Database()
QuartSchema(app)

@app.before_serving
async def startup():
    await database.init_db()

@app.after_serving
async def shutdown():
    await database.close_db()

@app.post("/contacts/")
@validate_request(ContactSchema)
@validate_response(ContactSchema)
async def create_contact(data: ContactSchema) -> ContactSchema:
    pass

def run() -> None:
    app.run(host="0.0.0.0")
