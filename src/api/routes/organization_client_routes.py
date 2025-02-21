from quart import Blueprint
from quart_schema import validate_request, validate_response, tag
from ..services import OrganizationClientService
from ..schemas import OrganizationClientRequestSchema, OrganizationClientResponseSchema, OrganizationClientListResponseSchema
from ..utils import ResponseHandler

organization_client_bp = Blueprint('organization_client', __name__)
organization_client_service = OrganizationClientService()

@organization_client_bp.route('/organization_clients', methods=['POST'])
@validate_request(OrganizationClientRequestSchema)
@validate_response(OrganizationClientResponseSchema, 201)
@tag(['OrganizationClient'])
async def create_organization_client(data: OrganizationClientRequestSchema):
    """
    Creates a new organization client with the provided data.
    """
    try:
        organization_client = await organization_client_service.create(data)
        response_data = OrganizationClientResponseSchema.model_validate(organization_client).model_dump()
        return ResponseHandler.success(response_data)
    except Exception as e:
        return ResponseHandler.exception(e)

@organization_client_bp.route('/organization_clients/<int:id>', methods=['GET'])
@validate_response(OrganizationClientResponseSchema)
@tag(['OrganizationClient'])
async def get_organization_client(id: int):
    """
    Retrieves an organization client by its ID.
    """
    try:
        organization_client = await organization_client_service.get_by_id(id)
        if organization_client:
            response_data = OrganizationClientResponseSchema.model_validate(organization_client).model_dump()
            return ResponseHandler.success(response_data)
        return ResponseHandler.error("Organization Client not found", 404)
    except Exception as e:
        return ResponseHandler.exception(e)

@organization_client_bp.route('/organization_clients', methods=['GET'])
@validate_response(OrganizationClientListResponseSchema)
@tag(['OrganizationClient'])
async def get_all_organization_clients():
    """
    Retrieves a list of all organization clients.
    """
    try:
        organization_clients = await organization_client_service.get_all()
        response_data = OrganizationClientListResponseSchema(items=[OrganizationClientResponseSchema.model_validate(organization_client).model_dump() for organization_client in organization_clients])
        return ResponseHandler.success(response_data.model_dump())
    except Exception as e:
        return ResponseHandler.exception(e)

@organization_client_bp.route('/organization_clients/<int:id>', methods=['PUT'])
@validate_request(OrganizationClientRequestSchema)
@validate_response(OrganizationClientResponseSchema)
@tag(['OrganizationClient'])
async def update_organization_client(id: int, data: OrganizationClientRequestSchema):
    """
    Updates an organization client by its ID.
    """
    try:
        organization_client = await organization_client_service.update(id, **data.model_dump())
        if organization_client:
            response_data = OrganizationClientResponseSchema.model_validate(organization_client).model_dump()
            return ResponseHandler.success(response_data)
        return ResponseHandler.error("Organization Client not found", 404)
    except Exception as e:
        return ResponseHandler.exception(e)

@organization_client_bp.route('/organization_clients/<int:id>', methods=['DELETE'])
@tag(['OrganizationClient'])
async def delete_organization_client(id: int):
    """
    Deletes an organization client by its ID.
    """
    try:
        success = await organization_client_service.delete(id)
        if success:
            return ResponseHandler.success(message="Organization Client deleted successfully")
        return ResponseHandler.error("Organization Client not found", 404)
    except Exception as e:
        return ResponseHandler.exception(e)