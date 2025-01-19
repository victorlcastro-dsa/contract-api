from quart import Quart
from .database import Database
from quart_bcrypt import Bcrypt
from . import routes
from . import main
from .config import QuartConfig, BcryptConfig, configure_schema

app = Quart(__name__)
app.config.from_object(QuartConfig)
app.config.from_object(BcryptConfig)

bcrypt = Bcrypt(app)
database = Database()
configure_schema(app)

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
