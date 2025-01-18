from quart import Quart
from quart_schema import QuartSchema, Info, Contact
from .database import Database
from quart_bcrypt import Bcrypt
from . import routes
from . import main
from .config import QuartConfig, BcryptConfig, QuartSchemaConfig

app = Quart(__name__)
app.config.from_object(QuartConfig)
app.config.from_object(BcryptConfig)

bcrypt = Bcrypt(app)
database = Database()
QuartSchema(app, info=Info(
    title=QuartSchemaConfig.TITLE,
    version=QuartSchemaConfig.VERSION,
    description=QuartSchemaConfig.DESCRIPTION,
    contact=Contact(
        email=QuartSchemaConfig.CONTACT_EMAIL,
        name=QuartSchemaConfig.CONTACT_NAME,
        url=QuartSchemaConfig.CONTACT_URL
    ),
    summary=QuartSchemaConfig.SUMMARY,
    terms_of_service=QuartSchemaConfig.TERMS_OF_SERVICE
), tags=QuartSchemaConfig.TAGS, conversion_preference=QuartSchemaConfig.CONVERSION_PREFERENCE)

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
