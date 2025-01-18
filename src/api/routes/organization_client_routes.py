from quart import Blueprint, request, jsonify
from quart_schema import validate_request, validate_response
from ..services import OrganizationClientService
from ..schemas import OrganizationClientRequestSchema, OrganizationClientResponseSchema, OrganizationClientListResponseSchema

organization_client_bp = Blueprint('organization_client', __name__)
organization_client_service = OrganizationClientService()

@organization_client_bp.route('/organization_clients', methods=['POST'])
@validate_request(OrganizationClientRequestSchema)
@validate_response(OrganizationClientResponseSchema, 201)
async def create_organization_client(data: OrganizationClientRequestSchema):
    organization_client = await organization_client_service.create(data)
    return jsonify(organization_client)

@organization_client_bp.route('/organization_clients/<int:id>', methods=['GET'])
@validate_response(OrganizationClientResponseSchema)
async def get_organization_client(id: int):
    organization_client = await organization_client_service.get_by_id(id)
    if organization_client:
        return jsonify(organization_client)
    return jsonify({"error": "Organization Client not found"}), 404

@organization_client_bp.route('/organization_clients', methods=['GET'])
@validate_response(OrganizationClientListResponseSchema)
async def get_all_organization_clients():
    organization_clients = await organization_client_service.get_all()
    return jsonify(organization_clients)

@organization_client_bp.route('/organization_clients/<int:id>', methods=['PUT'])
@validate_request(OrganizationClientRequestSchema)
@validate_response(OrganizationClientResponseSchema)
async def update_organization_client(id: int, data: OrganizationClientRequestSchema):
    organization_client = await organization_client_service.update(id, **data.model_dump())
    if organization_client:
        return jsonify(organization_client)
    return jsonify({"error": "Organization Client not found"}), 404

@organization_client_bp.route('/organization_clients/<int:id>', methods=['DELETE'])
async def delete_organization_client(id: int):
    success = await organization_client_service.delete(id)
    if success:
        return jsonify({"message": "Organization Client deleted successfully"})
    return jsonify({"error": "Organization Client not found"}), 404