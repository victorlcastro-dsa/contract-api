from quart_schema import QuartSchema, Info, Contact

class QuartConfig:
    """Configuration for Quart application."""
    DEBUG = True  # Enable debug mode

class BcryptConfig:
    """Configuration for Bcrypt."""
    BCRYPT_LOG_ROUNDS = 12  # Security configuration for Bcrypt

class QuartSchemaConfig:
    """Configuration for Quart Schema."""
    CONVERSION_PREFERENCE = 'pydantic'
    TITLE = "contract-api"
    VERSION = "0.1.0"
    DESCRIPTION = (
        "The `contract-api` is under development in Python using the Quart framework. "
        "It is designed to manage information related to contracts, offering routes for creating, retrieving, updating, and deleting data. "
        "The API will include features such as authentication, database integration, and various utility endpoints to handle contract management efficiently."
    )
    CONTACT_EMAIL = "victorlcastro.dsa@gmail.com"
    CONTACT_NAME = "Victor L. Castro"
    CONTACT_URL = "https://github.com/victorlcastro-dsa"
    SUMMARY = "A comprehensive API for managing contract-related information, built with the Quart framework."
    TERMS_OF_SERVICE = "https://github.com/victorlcastro-dsa/contract-api/blob/main/TERMS.md"
    TAGS = [
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
    ]

def configure_schema(app): # TODO: Move to a more appropriate location if necessary
    """Configure the Quart Schema for the application."""
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