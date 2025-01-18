from quart import Blueprint, request, jsonify
from quart_schema import validate_request, validate_response, tag
from ..services import UnionService
from ..schemas import UnionRequestSchema, UnionResponseSchema, UnionListResponseSchema

union_bp = Blueprint('union', __name__)
union_service = UnionService()

@union_bp.route('/unions', methods=['POST'])
@validate_request(UnionRequestSchema)
@validate_response(UnionResponseSchema, 201)
@tag(['Union'])
async def create_union(data: UnionRequestSchema):
    """
    Creates a new union with the provided data.
    """
    union = await union_service.create(data)
    response_data = UnionResponseSchema.model_validate(union).model_dump()
    return jsonify(response_data)

@union_bp.route('/unions/<int:id>', methods=['GET'])
@validate_response(UnionResponseSchema)
@tag(['Union'])
async def get_union(id: int):
    """
    Retrieves a union by its ID.
    """
    union = await union_service.get_by_id(id)
    if union:
        response_data = UnionResponseSchema.model_validate(union).model_dump()
        return response_data
    return jsonify({"error": "Union not found"}), 404

@union_bp.route('/unions', methods=['GET'])
@validate_response(UnionListResponseSchema)
@tag(['Union'])
async def get_all_unions():
    """
    Retrieves a list of all unions.
    """
    unions = await union_service.get_all()
    response_data = UnionListResponseSchema(items=[UnionResponseSchema.model_validate(union).model_dump() for union in unions])
    return response_data.model_dump()

@union_bp.route('/unions/<int:id>', methods=['PUT'])
@validate_request(UnionRequestSchema)
@validate_response(UnionResponseSchema)
@tag(['Union'])
async def update_union(id: int, data: UnionRequestSchema):
    """
    Updates a union by its ID.
    """
    union = await union_service.update(id, **data.model_dump())
    if union:
        response_data = UnionResponseSchema.model_validate(union).model_dump()
        return response_data
    return jsonify({"error": "Union not found"}), 404

@union_bp.route('/unions/<int:id>', methods=['DELETE'])
@tag(['Union'])
async def delete_union(id: int):
    """
    Deletes a union by its ID.
    """
    success = await union_service.delete(id)
    if success:
        return jsonify({"message": "Union deleted successfully"})
    return jsonify({"error": "Union not found"}), 404