from quart import Blueprint
from quart_schema import validate_request, validate_response, tag
from ..services import AdditionalService
from ..schemas import AdditionalRequestSchema, AdditionalResponseSchema, AdditionalListResponseSchema
from ..utils import ResponseHandler

additional_bp = Blueprint('additional', __name__)
additional_service = AdditionalService()

@additional_bp.route('/additionals', methods=['POST'])
@validate_request(AdditionalRequestSchema)
@validate_response(AdditionalResponseSchema, 201)
@tag(['Additional'])
async def create_additional(data: AdditionalRequestSchema):
    """
    Creates a new additional with the provided data.
    """
    try:
        additional = await additional_service.create(data)
        response_data = AdditionalResponseSchema.model_validate(additional).model_dump()
        return ResponseHandler.success(response_data)
    except Exception as e:
        return ResponseHandler.exception(e)

@additional_bp.route('/additionals/<int:id>', methods=['GET'])
@validate_response(AdditionalResponseSchema)
@tag(['Additional'])
async def get_additional(id: int):
    """
    Retrieves an additional by its ID.
    """
    try:
        additional = await additional_service.get_by_id(id)
        if additional:
            response_data = AdditionalResponseSchema.model_validate(additional).model_dump()
            return ResponseHandler.success(response_data)
        return ResponseHandler.error("Additional not found", 404)
    except Exception as e:
        return ResponseHandler.exception(e)

@additional_bp.route('/additionals', methods=['GET'])
@validate_response(AdditionalListResponseSchema)
@tag(['Additional'])
async def get_all_additionals():
    """
    Retrieves a list of all additionals.
    """
    try:
        additionals = await additional_service.get_all()
        response_data = AdditionalListResponseSchema(items=[AdditionalResponseSchema.model_validate(additional).model_dump() for additional in additionals])
        return ResponseHandler.success(response_data.model_dump())
    except Exception as e:
        return ResponseHandler.exception(e)

@additional_bp.route('/additionals/<int:id>', methods=['PUT'])
@validate_request(AdditionalRequestSchema)
@validate_response(AdditionalResponseSchema)
@tag(['Additional'])
async def update_additional(id: int, data: AdditionalRequestSchema):
    """
    Updates an additional by its ID.
    """
    try:
        additional = await additional_service.update(id, **data.model_dump())
        if additional:
            response_data = AdditionalResponseSchema.model_validate(additional).model_dump()
            return ResponseHandler.success(response_data)
        return ResponseHandler.error("Additional not found", 404)
    except Exception as e:
        return ResponseHandler.exception(e)

@additional_bp.route('/additionals/<int:id>', methods=['DELETE'])
@tag(['Additional'])
async def delete_additional(id: int):
    """
    Deletes an additional by its ID.
    """
    try:
        success = await additional_service.delete(id)
        if success:
            return ResponseHandler.success(message="Additional deleted successfully")
        return ResponseHandler.error("Additional not found", 404)
    except Exception as e:
        return ResponseHandler.exception(e)