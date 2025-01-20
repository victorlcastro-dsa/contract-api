from quart import Blueprint
from quart_schema import validate_request, validate_response, tag
from ..services import SeiService
from ..schemas import SeiRequestSchema, SeiResponseSchema, SeiListResponseSchema
from ..utils import ResponseHandler

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
    try:
        sei = await sei_service.create(data)
        response_data = SeiResponseSchema.model_validate(sei).model_dump()
        return ResponseHandler.success(response_data)
    except Exception as e:
        return ResponseHandler.exception(e)

@sei_bp.route('/seis/<int:id>', methods=['GET'])
@validate_response(SeiResponseSchema)
@tag(['Sei'])
async def get_sei(id: int):
    """
    Retrieves a SEI by its ID.
    """
    try:
        sei = await sei_service.get_by_id(id)
        if sei:
            response_data = SeiResponseSchema.model_validate(sei).model_dump()
            return ResponseHandler.success(response_data)
        return ResponseHandler.error("Sei not found", 404)
    except Exception as e:
        return ResponseHandler.exception(e)

@sei_bp.route('/seis', methods=['GET'])
@validate_response(SeiListResponseSchema)
@tag(['Sei'])
async def get_all_seis():
    """
    Retrieves a list of all SEIs.
    """
    try:
        seis = await sei_service.get_all()
        response_data = SeiListResponseSchema(items=[SeiResponseSchema.model_validate(sei).model_dump() for sei in seis])
        return ResponseHandler.success(response_data.model_dump())
    except Exception as e:
        return ResponseHandler.exception(e)

@sei_bp.route('/seis/<int:id>', methods=['PUT'])
@validate_request(SeiRequestSchema)
@validate_response(SeiResponseSchema)
@tag(['Sei'])
async def update_sei(id: int, data: SeiRequestSchema):
    """
    Updates a SEI by its ID.
    """
    try:
        sei = await sei_service.update(id, **data.model_dump())
        if sei:
            response_data = SeiResponseSchema.model_validate(sei).model_dump()
            return ResponseHandler.success(response_data)
        return ResponseHandler.error("Sei not found", 404)
    except Exception as e:
        return ResponseHandler.exception(e)

@sei_bp.route('/seis/<int:id>', methods=['DELETE'])
@tag(['Sei'])
async def delete_sei(id: int):
    """
    Deletes a SEI by its ID.
    """
    try:
        success = await sei_service.delete(id)
        if success:
            return ResponseHandler.success(message="Sei deleted successfully")
        return ResponseHandler.error("Sei not found", 404)
    except Exception as e:
        return ResponseHandler.exception(e)