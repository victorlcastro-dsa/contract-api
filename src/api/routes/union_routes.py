from quart import Blueprint, request, jsonify
from quart_schema import validate_request, validate_response
from ..services import UnionService
from ..schemas import UnionRequestSchema, UnionResponseSchema, UnionListResponseSchema

union_bp = Blueprint('union', __name__)
union_service = UnionService()

@union_bp.route('/unions', methods=['POST'])
@validate_request(UnionRequestSchema)
@validate_response(UnionResponseSchema, 201)
async def create_union(data: UnionRequestSchema):
    union = await union_service.create(data)
    return jsonify(union)

@union_bp.route('/unions/<int:id>', methods=['GET'])
@validate_response(UnionResponseSchema)
async def get_union(id: int):
    union = await union_service.get_by_id(id)
    if union:
        return jsonify(union)
    return jsonify({"error": "Union not found"}), 404

@union_bp.route('/unions', methods=['GET'])
@validate_response(UnionListResponseSchema)
async def get_all_unions():
    unions = await union_service.get_all()
    return jsonify(unions)

@union_bp.route('/unions/<int:id>', methods=['PUT'])
@validate_request(UnionRequestSchema)
@validate_response(UnionResponseSchema)
async def update_union(id: int, data: UnionRequestSchema):
    union = await union_service.update(id, **data.model_dump())
    if union:
        return jsonify(union)
    return jsonify({"error": "Union not found"}), 404

@union_bp.route('/unions/<int:id>', methods=['DELETE'])
async def delete_union(id: int):
    success = await union_service.delete(id)
    if success:
        return jsonify({"message": "Union deleted successfully"})
    return jsonify({"error": "Union not found"}), 404