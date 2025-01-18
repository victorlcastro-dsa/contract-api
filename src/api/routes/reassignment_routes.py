from quart import Blueprint, request, jsonify
from quart_schema import validate_request, validate_response
from ..services import ReassignmentService
from ..schemas import ReassignmentRequestSchema, ReassignmentResponseSchema, ReassignmentListResponseSchema

reassignment_bp = Blueprint('reassignment', __name__)
reassignment_service = ReassignmentService()

@reassignment_bp.route('/reassignments', methods=['POST'])
@validate_request(ReassignmentRequestSchema)
@validate_response(ReassignmentResponseSchema, 201)
async def create_reassignment(data: ReassignmentRequestSchema):
    reassignment = await reassignment_service.create(data)
    return jsonify(reassignment)

@reassignment_bp.route('/reassignments/<int:id>', methods=['GET'])
@validate_response(ReassignmentResponseSchema)
async def get_reassignment(id: int):
    reassignment = await reassignment_service.get_by_id(id)
    if reassignment:
        return jsonify(reassignment)
    return jsonify({"error": "Reassignment not found"}), 404

@reassignment_bp.route('/reassignments', methods=['GET'])
@validate_response(ReassignmentListResponseSchema)
async def get_all_reassignments():
    reassignments = await reassignment_service.get_all()
    return jsonify(reassignments)

@reassignment_bp.route('/reassignments/<int:id>', methods=['PUT'])
@validate_request(ReassignmentRequestSchema)
@validate_response(ReassignmentResponseSchema)
async def update_reassignment(id: int, data: ReassignmentRequestSchema):
    reassignment = await reassignment_service.update(id, **data.model_dump())
    if reassignment:
        return jsonify(reassignment)
    return jsonify({"error": "Reassignment not found"}), 404

@reassignment_bp.route('/reassignments/<int:id>', methods=['DELETE'])
async def delete_reassignment(id: int):
    success = await reassignment_service.delete(id)
    if success:
        return jsonify({"message": "Reassignment deleted successfully"})
    return jsonify({"error": "Reassignment not found"}), 404