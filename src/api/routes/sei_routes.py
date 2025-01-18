from quart import Blueprint, request, jsonify
from quart_schema import validate_request, validate_response
from ..services import SeiService
from ..schemas import SeiRequestSchema, SeiResponseSchema, SeiListResponseSchema

sei_bp = Blueprint('sei', __name__)
sei_service = SeiService()

@sei_bp.route('/seis', methods=['POST'])
@validate_request(SeiRequestSchema)
@validate_response(SeiResponseSchema, 201)
async def create_sei(data: SeiRequestSchema):
    sei = await sei_service.create(data)
    return jsonify(sei)

@sei_bp.route('/seis/<int:id>', methods=['GET'])
@validate_response(SeiResponseSchema)
async def get_sei(id: int):
    sei = await sei_service.get_by_id(id)
    if sei:
        return jsonify(sei)
    return jsonify({"error": "Sei not found"}), 404

@sei_bp.route('/seis', methods=['GET'])
@validate_response(SeiListResponseSchema)
async def get_all_seis():
    seis = await sei_service.get_all()
    return jsonify(seis)

@sei_bp.route('/seis/<int:id>', methods=['PUT'])
@validate_request(SeiRequestSchema)
@validate_response(SeiResponseSchema)
async def update_sei(id: int, data: SeiRequestSchema):
    sei = await sei_service.update(id, **data.model_dump())
    if sei:
        return jsonify(sei)
    return jsonify({"error": "Sei not found"}), 404

@sei_bp.route('/seis/<int:id>', methods=['DELETE'])
async def delete_sei(id: int):
    success = await sei_service.delete(id)
    if success:
        return jsonify({"message": "Sei deleted successfully"})
    return jsonify({"error": "Sei not found"}), 404