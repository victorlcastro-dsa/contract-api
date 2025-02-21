from quart import Blueprint
from quart_schema import validate_request, validate_response, tag
from ..services import ContactService
from ..schemas import ContactRequestSchema, ContactResponseSchema, ContactListResponseSchema
from ..utils import ResponseHandler

contact_bp = Blueprint('contact', __name__)
contact_service = ContactService()

@contact_bp.route('/contacts', methods=['POST'])
@validate_request(ContactRequestSchema)
@validate_response(ContactResponseSchema, 201)
@tag(['Contact'])
async def create_contact(data: ContactRequestSchema):
    """
    Creates a new contact with the provided data.
    """
    try:
        contact = await contact_service.create(data)
        response_data = ContactResponseSchema.model_validate(contact).model_dump()
        return ResponseHandler.success(response_data)
    except Exception as e:
        return ResponseHandler.exception(e)

@contact_bp.route('/contacts/<int:id>', methods=['GET'])
@validate_response(ContactResponseSchema)
@tag(['Contact'])
async def get_contact(id: int):
    """
    Retrieves a contact by its ID.
    """
    try:
        contact = await contact_service.get_by_id(id)
        if contact:
            response_data = ContactResponseSchema.model_validate(contact).model_dump()
            return ResponseHandler.success(response_data)
        return ResponseHandler.error("Contact not found", 404)
    except Exception as e:
        return ResponseHandler.exception(e)

@contact_bp.route('/contacts', methods=['GET'])
@validate_response(ContactListResponseSchema)
@tag(['Contact'])
async def get_all_contacts():
    """
    Retrieves a list of all contacts.
    """
    try:
        contacts = await contact_service.get_all()
        response_data = ContactListResponseSchema(items=[ContactResponseSchema.model_validate(contact).model_dump() for contact in contacts])
        return ResponseHandler.success(response_data.model_dump())
    except Exception as e:
        return ResponseHandler.exception(e)

@contact_bp.route('/contacts/<int:id>', methods=['PUT'])
@validate_request(ContactRequestSchema)
@validate_response(ContactResponseSchema)
@tag(['Contact'])
async def update_contact(id: int, data: ContactRequestSchema):
    """
    Updates a contact by its ID.
    """
    try:
        contact = await contact_service.update(id, **data.model_dump())
        if contact:
            response_data = ContactResponseSchema.model_validate(contact).model_dump()
            return ResponseHandler.success(response_data)
        return ResponseHandler.error("Contact not found", 404)
    except Exception as e:
        return ResponseHandler.exception(e)

@contact_bp.route('/contacts/<int:id>', methods=['DELETE'])
@tag(['Contact'])
async def delete_contact(id: int):
    """
    Deletes a contact by its ID.
    """
    try:
        success = await contact_service.delete(id)
        if success:
            return ResponseHandler.success(message="Contact deleted successfully")
        return ResponseHandler.error("Contact not found", 404)
    except Exception as e:
        return ResponseHandler.exception(e)