from quart import Blueprint, request, jsonify
from quart_schema import validate_request, validate_response, tag
from ..services import SeiService
from ..schemas import SeiRequestSchema, SeiResponseSchema, SeiListResponseSchema

sei_bp = Blueprint('sei', __name__)
sei_service = SeiService()

@sei_bp.route('/seis', methods=['POST'])
@validate_request(SeiRequestSchema)
@validate_response(SeiResponseSchema, 201)
@tag(['Sei'])
async def create_sei(data: SeiRequestSchema):
    """
    Creates a new SEI with the provided data.
    """
    sei = await sei_service.create(data)
    response_data = SeiResponseSchema.model_validate(sei).model_dump()
    return jsonify(response_data)

@sei_bp.route('/seis/<int:id>', methods=['GET'])
@validate_response(SeiResponseSchema)
@tag(['Sei'])
async def get_sei(id: int):
    """
    Retrieves a SEI by its ID.
    """
    sei = await sei_service.get_by_id(id)
    if sei:
        response_data = SeiResponseSchema.model_validate(sei).model_dump()
        return response_data
    return jsonify({"error": "Sei not found"}), 404

@sei_bp.route('/seis', methods=['GET'])
@validate_response(SeiListResponseSchema)
@tag(['Sei'])
async def get_all_seis():
    """
    Retrieves a list of all SEIs.
    """
    seis = await sei_service.get_all()
    response_data = SeiListResponseSchema(items=[SeiResponseSchema.model_validate(sei).model_dump() for sei in seis])
    return response_data.model_dump()

@sei_bp.route('/seis/<int:id>', methods=['PUT'])
@validate_request(SeiRequestSchema)
@validate_response(SeiResponseSchema)
@tag(['Sei'])
async def update_sei(id: int, data: SeiRequestSchema):
    """
    Updates a SEI by its ID.
    """
    sei = await sei_service.update(id, **data.model_dump())
    if sei:
        response_data = SeiResponseSchema.model_validate(sei).model_dump()
        return response_data
    return jsonify({"error": "Sei not found"}), 404

@sei_bp.route('/seis/<int:id>', methods=['DELETE'])
@tag(['Sei'])
async def delete_sei(id: int):
    """
    Deletes a SEI by its ID.
    """
    success = await sei_service.delete(id)
    if success:
        return jsonify({"message": "Sei deleted successfully"})
    return jsonify({"error": "Sei not found"}), 404