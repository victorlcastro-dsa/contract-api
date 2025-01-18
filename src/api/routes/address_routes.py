from quart import Blueprint, request, jsonify
from quart_schema import validate_request, validate_response
from ..services import AddressService
from ..schemas import AddressRequestSchema, AddressResponseSchema, AddressListResponseSchema

address_bp = Blueprint('address', __name__)
address_service = AddressService()

@address_bp.route('/addresses', methods=['POST'])
@validate_request(AddressRequestSchema)
@validate_response(AddressResponseSchema, 201)
async def create_address(data: AddressRequestSchema):
    address = await address_service.create(data)
    return jsonify(address)

@address_bp.route('/addresses/<int:id>', methods=['GET'])
@validate_response(AddressResponseSchema)
async def get_address(id: int):
    address = await address_service.get_by_id(id)
    if address:
        return jsonify(address)
    return jsonify({"error": "Address not found"}), 404

@address_bp.route('/addresses', methods=['GET'])
@validate_response(AddressListResponseSchema)
async def get_all_addresses():
    addresses = await address_service.get_all()
    return jsonify(addresses)

@address_bp.route('/addresses/<int:id>', methods=['PUT'])
@validate_request(AddressRequestSchema)
@validate_response(AddressResponseSchema)
async def update_address(id: int, data: AddressRequestSchema):
    address = await address_service.update(id, **data.model_dump())
    if address:
        return jsonify(address)
    return jsonify({"error": "Address not found"}), 404

@address_bp.route('/addresses/<int:id>', methods=['DELETE'])
async def delete_address(id: int):
    success = await address_service.delete(id)
    if success:
        return jsonify({"message": "Address deleted successfully"})
    return jsonify({"error": "Address not found"}), 404