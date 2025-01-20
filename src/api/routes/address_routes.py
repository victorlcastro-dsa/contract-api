from quart import Blueprint
from quart_schema import validate_request, validate_response, tag
from ..services import AddressService
from ..schemas import AddressRequestSchema, AddressResponseSchema, AddressListResponseSchema
from ..utils import ResponseHandler

address_bp = Blueprint('address', __name__)
address_service = AddressService()

@address_bp.route('/addresses', methods=['POST'])
@validate_request(AddressRequestSchema)
@validate_response(AddressResponseSchema, 201)
@tag(['Address'])
async def create_address(data: AddressRequestSchema):
    """
    Creates a new address with the provided data.
    """
    try:
        address = await address_service.create(data)
        response_data = AddressResponseSchema.model_validate(address).model_dump()
        return ResponseHandler.success(response_data)
    except Exception as e:
        return ResponseHandler.exception(e)

@address_bp.route('/addresses/<int:id>', methods=['GET'])
@validate_response(AddressResponseSchema)
@tag(['Address'])
async def get_address(id: int):
    """
    Retrieves an address by its ID.
    """
    try:
        address = await address_service.get_by_id(id)
        if address:
            response_data = AddressResponseSchema.model_validate(address).model_dump()
            return ResponseHandler.success(response_data)
        return ResponseHandler.error("Address not found", 404)
    except Exception as e:
        return ResponseHandler.exception(e)

@address_bp.route('/addresses', methods=['GET'])
@validate_response(AddressListResponseSchema)
@tag(['Address'])
async def get_all_addresses():
    """
    Retrieves a list of all addresses.
    """
    try:
        addresses = await address_service.get_all()
        response_data = AddressListResponseSchema(items=[AddressResponseSchema.model_validate(address).model_dump() for address in addresses])
        return ResponseHandler.success(response_data.model_dump())
    except Exception as e:
        return ResponseHandler.exception(e)

@address_bp.route('/addresses/<int:id>', methods=['PUT'])
@validate_request(AddressRequestSchema)
@validate_response(AddressResponseSchema)
@tag(['Address'])
async def update_address(id: int, data: AddressRequestSchema):
    """
    Updates an address by its ID.
    """
    try:
        address = await address_service.update(id, **data.model_dump())
        if address:
            response_data = AddressResponseSchema.model_validate(address).model_dump()
            return ResponseHandler.success(response_data)
        return ResponseHandler.error("Address not found", 404)
    except Exception as e:
        return ResponseHandler.exception(e)

@address_bp.route('/addresses/<int:id>', methods=['DELETE'])
@tag(['Address'])
async def delete_address(id: int):
    """
    Deletes an address by its ID.
    """
    try:
        success = await address_service.delete(id)
        if success:
            return ResponseHandler.success(message="Address deleted successfully")
        return ResponseHandler.error("Address not found", 404)
    except Exception as e:
        return ResponseHandler.exception(e)