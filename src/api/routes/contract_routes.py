from quart import Blueprint, request, jsonify
from quart_schema import validate_request, validate_response
from ..services import ContractService
from ..schemas import ContractRequestSchema, ContractResponseSchema, ContractListResponseSchema

contract_bp = Blueprint('contract', __name__)
contract_service = ContractService()

@contract_bp.route('/contracts', methods=['POST'])
@validate_request(ContractRequestSchema)
@validate_response(ContractResponseSchema, 201)
async def create_contract(data: ContractRequestSchema):
    contract = await contract_service.create(data)
    return jsonify(contract)

@contract_bp.route('/contracts/<int:id>', methods=['GET'])
@validate_response(ContractResponseSchema)
async def get_contract(id: int):
    contract = await contract_service.get_by_id(id)
    if contract:
        return jsonify(contract)
    return jsonify({"error": "Contract not found"}), 404

@contract_bp.route('/contracts', methods=['GET'])
@validate_response(ContractListResponseSchema)
async def get_all_contracts():
    contracts = await contract_service.get_all()
    return jsonify(contracts)

@contract_bp.route('/contracts/<int:id>', methods=['PUT'])
@validate_request(ContractRequestSchema)
@validate_response(ContractResponseSchema)
async def update_contract(id: int, data: ContractRequestSchema):
    contract = await contract_service.update(id, **data.model_dump())
    if contract:
        return jsonify(contract)
    return jsonify({"error": "Contract not found"}), 404

@contract_bp.route('/contracts/<int:id>', methods=['DELETE'])
async def delete_contract(id: int):
    success = await contract_service.delete(id)
    if success:
        return jsonify({"message": "Contract deleted successfully"})
    return jsonify({"error": "Contract not found"}), 404