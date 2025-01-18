from quart import Blueprint, request, jsonify
from quart_schema import validate_request, validate_response
from ..services import RoleService
from ..schemas import RoleRequestSchema, RoleResponseSchema, RoleListResponseSchema

role_bp = Blueprint('role', __name__)
role_service = RoleService()

@role_bp.route('/roles', methods=['POST'])
@validate_request(RoleRequestSchema)
@validate_response(RoleResponseSchema, 201)
async def create_role(data: RoleRequestSchema):
    role = await role_service.create(data)
    return jsonify(role)

@role_bp.route('/roles/<int:id>', methods=['GET'])
@validate_response(RoleResponseSchema)
async def get_role(id: int):
    role = await role_service.get_by_id(id)
    if role:
        return jsonify(role)
    return jsonify({"error": "Role not found"}), 404

@role_bp.route('/roles', methods=['GET'])
@validate_response(RoleListResponseSchema)
async def get_all_roles():
    roles = await role_service.get_all()
    return jsonify(roles)

@role_bp.route('/roles/<int:id>', methods=['PUT'])
@validate_request(RoleRequestSchema)
@validate_response(RoleResponseSchema)
async def update_role(id: int, data: RoleRequestSchema):
    role = await role_service.update(id, **data.model_dump())
    if role:
        return jsonify(role)
    return jsonify({"error": "Role not found"}), 404

@role_bp.route('/roles/<int:id>', methods=['DELETE'])
async def delete_role(id: int):
    success = await role_service.delete(id)
    if success:
        return jsonify({"message": "Role deleted successfully"})
    return jsonify({"error": "Role not found"}), 404