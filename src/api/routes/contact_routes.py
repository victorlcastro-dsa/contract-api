from quart import Blueprint, request, jsonify
from quart_schema import validate_request, validate_response
from ..services import ContactService
from ..schemas import ContactRequestSchema, ContactResponseSchema, ContactListResponseSchema

contact_bp = Blueprint('contact', __name__)
contact_service = ContactService()

@contact_bp.route('/contacts', methods=['POST'])
@validate_request(ContactRequestSchema)
@validate_response(ContactResponseSchema, 201)
async def create_contact(data: ContactRequestSchema):
    contact = await contact_service.create(data)
    return jsonify(contact)

@contact_bp.route('/contacts/<int:id>', methods=['GET'])
@validate_response(ContactResponseSchema)
async def get_contact(id: int):
    contact = await contact_service.get_by_id(id)
    if contact:
        return jsonify(contact)
    return jsonify({"error": "Contact not found"}), 404

@contact_bp.route('/contacts', methods=['GET'])
@validate_response(ContactListResponseSchema)
async def get_all_contacts():
    contacts = await contact_service.get_all()
    return jsonify(contacts)

@contact_bp.route('/contacts/<int:id>', methods=['PUT'])
@validate_request(ContactRequestSchema)
@validate_response(ContactResponseSchema)
async def update_contact(id: int, data: ContactRequestSchema):
    contact = await contact_service.update(id, **data.model_dump())
    if contact:
        return jsonify(contact)
    return jsonify({"error": "Contact not found"}), 404

@contact_bp.route('/contacts/<int:id>', methods=['DELETE'])
async def delete_contact(id: int):
    success = await contact_service.delete(id)
    if success:
        return jsonify({"message": "Contact deleted successfully"})
    return jsonify({"error": "Contact not found"}), 404