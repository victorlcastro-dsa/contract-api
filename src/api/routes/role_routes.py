from quart import Blueprint, request, jsonify
from quart_schema import validate_request, validate_response, tag
from ..services import RoleService
from ..schemas import RoleRequestSchema, RoleResponseSchema, RoleListResponseSchema

role_bp = Blueprint('role', __name__)
role_service = RoleService()

@role_bp.route('/roles', methods=['POST'])
@validate_request(RoleRequestSchema)
@validate_response(RoleResponseSchema, 201)
@tag(['Role'])
async def create_role(data: RoleRequestSchema):
    """
    Creates a new role with the provided data.
    """
    role = await role_service.create(data)
    response_data = RoleResponseSchema.model_validate(role).model_dump()
    return jsonify(response_data)

@role_bp.route('/roles/<int:id>', methods=['GET'])
@validate_response(RoleResponseSchema)
@tag(['Role'])
async def get_role(id: int):
    """
    Retrieves a role by its ID.
    """
    role = await role_service.get_by_id(id)
    if role:
        response_data = RoleResponseSchema.model_validate(role).model_dump()
        return response_data
    return jsonify({"error": "Role not found"}), 404

@role_bp.route('/roles', methods=['GET'])
@validate_response(RoleListResponseSchema)
@tag(['Role'])
async def get_all_roles():
    """
    Retrieves a list of all roles.
    """
    roles = await role_service.get_all()
    response_data = RoleListResponseSchema(items=[RoleResponseSchema.model_validate(role).model_dump() for role in roles])
    return response_data.model_dump()

@role_bp.route('/roles/<int:id>', methods=['PUT'])
@validate_request(RoleRequestSchema)
@validate_response(RoleResponseSchema)
@tag(['Role'])
async def update_role(id: int, data: RoleRequestSchema):
    """
    Updates a role by its ID.
    """
    role = await role_service.update(id, **data.model_dump())
    if role:
        response_data = RoleResponseSchema.model_validate(role).model_dump()
        return response_data
    return jsonify({"error": "Role not found"}), 404

@role_bp.route('/roles/<int:id>', methods=['DELETE'])
@tag(['Role'])
async def delete_role(id: int):
    """
    Deletes a role by its ID.
    """
    success = await role_service.delete(id)
    if success:
        return jsonify({"message": "Role deleted successfully"})
    return jsonify({"error": "Role not found"}), 404