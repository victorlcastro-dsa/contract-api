from quart import Quart, request, jsonify
from quart_schema import QuartSchema, validate_request, validate_response
from .database import Database
from quart_bcrypt import Bcrypt
from . import routes
from . import main

app = Quart(__name__)
app.config["DEBUG"] = True  # Enable debug mode
app.config["BCRYPT_LOG_ROUNDS"] = 12  # Security configuration for Bcrypt

bcrypt = Bcrypt(app)
database = Database()
QuartSchema(app)

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
