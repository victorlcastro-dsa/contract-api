from quart import Quart, request, jsonify
from quart_schema import QuartSchema, validate_request, validate_response, Info, Contact
from .database import Database
from quart_bcrypt import Bcrypt
from . import routes
from . import main

app = Quart(__name__)
app.config["DEBUG"] = True  # Enable debug mode
app.config["BCRYPT_LOG_ROUNDS"] = 12  # Security configuration for Bcrypt

bcrypt = Bcrypt(app)
database = Database()
QuartSchema(app, info=Info(
    title="contract-api",
    version="0.1.0",
    description="The `contract-api` is developed in Python using the Quart framework. It is designed to manage information related to contracts, offering routes for creating, retrieving, updating, and deleting data. The API includes features such as authentication, database integration, and various utility endpoints to handle contract management efficiently.",
    contact=Contact(
        email="victorlcastro.dsa@gmail.com",
        name="Victor L. Castro",
        url="https://github.com/victorlcastro-dsa"
    ),
    summary="A comprehensive API for managing contract-related information, built with the Quart framework.",
    terms_of_service="https://github.com/victorlcastro-dsa/contract-api/blob/main/TERMS.md"
), tags=[
    {"name": "Main", "description": "Main routes for the API, including health check and API information."},
    {"name": "Union", "description": "Management of unions, including creation, retrieval, updating, and deletion of unions."},
    {"name": "Sei", "description": "Management of SEIs, including creation, retrieval, updating, and deletion of SEIs."},
    {"name": "Address", "description": "Management of addresses, including creation, retrieval, updating, and deletion of addresses."},
    {"name": "OrganizationClient", "description": "Management of organization clients, including creation, retrieval, updating, and deletion of organization clients."},
    {"name": "Contract", "description": "Management of contracts, including creation, retrieval, updating, and deletion of contracts."},
    {"name": "Attachment", "description": "Management of attachments, including creation, retrieval, updating, and deletion of attachments."},
    {"name": "GeneralInformation", "description": "Management of general information, including creation, retrieval, updating, and deletion of general information."},
    {"name": "Item", "description": "Management of items, including creation, retrieval, updating, and deletion of items."},
    {"name": "Role", "description": "Management of roles, including creation, retrieval, updating, and deletion of roles."},
    {"name": "Reassignment", "description": "Management of reassignments, including creation, retrieval, updating, and deletion of reassignments."},
    {"name": "Additional", "description": "Management of additionals, including creation, retrieval, updating, and deletion of additionals."},
    {"name": "Contact", "description": "Management of contacts, including creation, retrieval, updating, and deletion of contacts."}
],
conversion_preference='pydantic')

# Registrar os blueprints
app.register_blueprint(main.main_bp)
app.register_blueprint(routes.additional_bp)
app.register_blueprint(routes.address_bp)
app.register_blueprint(routes.attachment_bp)
app.register_blueprint(routes.contact_bp)
app.register_blueprint(routes.contract_bp)
app.register_blueprint(routes.general_information_bp)
app.register_blueprint(routes.item_bp)
app.register_blueprint(routes.organization_client_bp)
app.register_blueprint(routes.reassignment_bp)
app.register_blueprint(routes.role_bp)
app.register_blueprint(routes.sei_bp)
app.register_blueprint(routes.union_bp)

@app.before_serving
async def startup():
    await database.init_db()

@app.after_serving
async def shutdown():
    await database.close_db()

def run() -> None:
    app.run(host="0.0.0.0")
