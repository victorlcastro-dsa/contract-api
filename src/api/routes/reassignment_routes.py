from quart import Blueprint
from quart_schema import validate_request, validate_response, tag
from ..services import ReassignmentService
from ..schemas import ReassignmentRequestSchema, ReassignmentResponseSchema, ReassignmentListResponseSchema
from ..utils import ResponseHandler

reassignment_bp = Blueprint('reassignment', __name__)
reassignment_service = ReassignmentService()

@reassignment_bp.route('/reassignments', methods=['POST'])
@validate_request(ReassignmentRequestSchema)
@validate_response(ReassignmentResponseSchema, 201)
@tag(['Reassignment'])
async def create_reassignment(data: ReassignmentRequestSchema):
    """
    Creates a new reassignment with the provided data.
    """
    try:
        reassignment = await reassignment_service.create(data)
        response_data = ReassignmentResponseSchema.model_validate(reassignment).model_dump()
        return ResponseHandler.success(response_data)
    except Exception as e:
        return ResponseHandler.exception(e)

@reassignment_bp.route('/reassignments/<int:id>', methods=['GET'])
@validate_response(ReassignmentResponseSchema)
@tag(['Reassignment'])
async def get_reassignment(id: int):
    """
    Retrieves a reassignment by its ID.
    """
    try:
        reassignment = await reassignment_service.get_by_id(id)
        if reassignment:
            response_data = ReassignmentResponseSchema.model_validate(reassignment).model_dump()
            return ResponseHandler.success(response_data)
        return ResponseHandler.error("Reassignment not found", 404)
    except Exception as e:
        return ResponseHandler.exception(e)

@reassignment_bp.route('/reassignments', methods=['GET'])
@validate_response(ReassignmentListResponseSchema)
@tag(['Reassignment'])
async def get_all_reassignments():
    """
    Retrieves a list of all reassignments.
    """
    try:
        reassignments = await reassignment_service.get_all()
        response_data = ReassignmentListResponseSchema(items=[ReassignmentResponseSchema.model_validate(reassignment).model_dump() for reassignment in reassignments])
        return ResponseHandler.success(response_data.model_dump())
    except Exception as e:
        return ResponseHandler.exception(e)

@reassignment_bp.route('/reassignments/<int:id>', methods=['PUT'])
@validate_request(ReassignmentRequestSchema)
@validate_response(ReassignmentResponseSchema)
@tag(['Reassignment'])
async def update_reassignment(id: int, data: ReassignmentRequestSchema):
    """
    Updates a reassignment by its ID.
    """
    try:
        reassignment = await reassignment_service.update(id, **data.model_dump())
        if reassignment:
            response_data = ReassignmentResponseSchema.model_validate(reassignment).model_dump()
            return ResponseHandler.success(response_data)
        return ResponseHandler.error("Reassignment not found", 404)
    except Exception as e:
        return ResponseHandler.exception(e)

@reassignment_bp.route('/reassignments/<int:id>', methods=['DELETE'])
@tag(['Reassignment'])
async def delete_reassignment(id: int):
    """
    Deletes a reassignment by its ID.
    """
    try:
        success = await reassignment_service.delete(id)
        if success:
            return ResponseHandler.success(message="Reassignment deleted successfully")
        return ResponseHandler.error("Reassignment not found", 404)
    except Exception as e:
        return ResponseHandler.exception(e)