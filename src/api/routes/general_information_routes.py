from quart import Blueprint, request, jsonify
from quart_schema import validate_request, validate_response, tag
from ..services import GeneralInformationService
from ..schemas import GeneralInformationRequestSchema, GeneralInformationResponseSchema, GeneralInformationListResponseSchema

general_information_bp = Blueprint('general_information', __name__)
general_information_service = GeneralInformationService()

@general_information_bp.route('/general_informations', methods=['POST'])
@validate_request(GeneralInformationRequestSchema)
@validate_response(GeneralInformationResponseSchema, 201)
@tag(['GeneralInformation'])
async def create_general_information(data: GeneralInformationRequestSchema):
    """
    Creates a new general information with the provided data.
    """
    general_information = await general_information_service.create(data)
    response_data = GeneralInformationResponseSchema.model_validate(general_information).model_dump()
    return jsonify(response_data)

@general_information_bp.route('/general_informations/<int:id>', methods=['GET'])
@validate_response(GeneralInformationResponseSchema)
@tag(['GeneralInformation'])
async def get_general_information(id: int):
    """
    Retrieves a general information by its ID.
    """
    general_information = await general_information_service.get_by_id(id)
    if general_information:
        response_data = GeneralInformationResponseSchema.model_validate(general_information).model_dump()
        return response_data
    return jsonify({"error": "General Information not found"}), 404

@general_information_bp.route('/general_informations', methods=['GET'])
@validate_response(GeneralInformationListResponseSchema)
@tag(['GeneralInformation'])
async def get_all_general_informations():
    """
    Retrieves a list of all general informations.
    """
    general_informations = await general_information_service.get_all()
    response_data = GeneralInformationListResponseSchema(items=[GeneralInformationResponseSchema.model_validate(general_information).model_dump() for general_information in general_informations])
    return response_data.model_dump()

@general_information_bp.route('/general_informations/<int:id>', methods=['PUT'])
@validate_request(GeneralInformationRequestSchema)
@validate_response(GeneralInformationResponseSchema)
@tag(['GeneralInformation'])
async def update_general_information(id: int, data: GeneralInformationRequestSchema):
    """
    Updates a general information by its ID.
    """
    general_information = await general_information_service.update(id, **data.model_dump())
    if general_information:
        response_data = GeneralInformationResponseSchema.model_validate(general_information).model_dump()
        return response_data
    return jsonify({"error": "General Information not found"}), 404

@general_information_bp.route('/general_informations/<int:id>', methods=['DELETE'])
@tag(['GeneralInformation'])
async def delete_general_information(id: int):
    """
    Deletes a general information by its ID.
    """
    success = await general_information_service.delete(id)
    if success:
        return jsonify({"message": "General Information deleted successfully"})
    return jsonify({"error": "General Information not found"}), 404