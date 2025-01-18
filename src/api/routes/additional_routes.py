from quart import Blueprint, request, jsonify
from quart_schema import validate_request, validate_response
from ..services import AdditionalService
from ..schemas import AdditionalRequestSchema, AdditionalResponseSchema, AdditionalListResponseSchema

additional_bp = Blueprint('additional', __name__)
additional_service = AdditionalService()

@additional_bp.route('/additionals', methods=['POST'])
@validate_request(AdditionalRequestSchema)
@validate_response(AdditionalResponseSchema, 201)
async def create_additional(data: AdditionalRequestSchema):
    additional = await additional_service.create(data)
    return jsonify(additional)

@additional_bp.route('/additionals/<int:id>', methods=['GET'])
@validate_response(AdditionalResponseSchema)
async def get_additional(id: int):
    additional = await additional_service.get_by_id(id)
    if additional:
        return jsonify(additional)
    return jsonify({"error": "Additional not found"}), 404

@additional_bp.route('/additionals', methods=['GET'])
@validate_response(AdditionalListResponseSchema)
async def get_all_additionals():
    additionals = await additional_service.get_all()
    return jsonify(additionals)

@additional_bp.route('/additionals/<int:id>', methods=['PUT'])
@validate_request(AdditionalRequestSchema)
@validate_response(AdditionalResponseSchema)
async def update_additional(id: int, data: AdditionalRequestSchema):
    additional = await additional_service.update(id, **data.model_dump())
    if additional:
        return jsonify(additional)
    return jsonify({"error": "Additional not found"}), 404

@additional_bp.route('/additionals/<int:id>', methods=['DELETE'])
async def delete_additional(id: int):
    success = await additional_service.delete(id)
    if success:
        return jsonify({"message": "Additional deleted successfully"})
    return jsonify({"error": "Additional not found"}), 404