from quart import Blueprint, request, jsonify
from quart_schema import validate_request, validate_response
from ..services import GeneralInformationService
from ..schemas import GeneralInformationRequestSchema, GeneralInformationResponseSchema, GeneralInformationListResponseSchema

general_information_bp = Blueprint('general_information', __name__)
general_information_service = GeneralInformationService()

@general_information_bp.route('/general_informations', methods=['POST'])
@validate_request(GeneralInformationRequestSchema)
@validate_response(GeneralInformationResponseSchema, 201)
async def create_general_information(data: GeneralInformationRequestSchema):
    general_information = await general_information_service.create(data)
    return jsonify(general_information)

@general_information_bp.route('/general_informations/<int:id>', methods=['GET'])
@validate_response(GeneralInformationResponseSchema)
async def get_general_information(id: int):
    general_information = await general_information_service.get_by_id(id)
    if general_information:
        return jsonify(general_information)
    return jsonify({"error": "General Information not found"}), 404

@general_information_bp.route('/general_informations', methods=['GET'])
@validate_response(GeneralInformationListResponseSchema)
async def get_all_general_informations():
    general_informations = await general_information_service.get_all()
    return jsonify(general_informations)

@general_information_bp.route('/general_informations/<int:id>', methods=['PUT'])
@validate_request(GeneralInformationRequestSchema)
@validate_response(GeneralInformationResponseSchema)
async def update_general_information(id: int, data: GeneralInformationRequestSchema):
    general_information = await general_information_service.update(id, **data.model_dump())
    if general_information:
        return jsonify(general_information)
    return jsonify({"error": "General Information not found"}), 404

@general_information_bp.route('/general_informations/<int:id>', methods=['DELETE'])
async def delete_general_information(id: int):
    success = await general_information_service.delete(id)
    if success:
        return jsonify({"message": "General Information deleted successfully"})
    return jsonify({"error": "General Information not found"}), 404