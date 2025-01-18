from quart import Blueprint, request, jsonify
from quart_schema import validate_request, validate_response, tag
from ..services import ContractService
from ..schemas import ContractRequestSchema, ContractResponseSchema, ContractListResponseSchema

contract_bp = Blueprint('contract', __name__)
contract_service = ContractService()

@contract_bp.route('/contracts', methods=['POST'])
@validate_request(ContractRequestSchema)
@validate_response(ContractResponseSchema, 201)
@tag(['Contract'])
async def create_contract(data: ContractRequestSchema):
    """
    Creates a new contract with the provided data.
    """
    contract = await contract_service.create(data)
    response_data = ContractResponseSchema.model_validate(contract).model_dump()
    return jsonify(response_data)

@contract_bp.route('/contracts/<int:id>', methods=['GET'])
@validate_response(ContractResponseSchema)
@tag(['Contract'])
async def get_contract(id: int):
    """
    Retrieves a contract by its ID.
    """
    contract = await contract_service.get_by_id(id)
    if contract:
        response_data = ContractResponseSchema.model_validate(contract).model_dump()
        return response_data
    return jsonify({"error": "Contract not found"}), 404

@contract_bp.route('/contracts', methods=['GET'])
@validate_response(ContractListResponseSchema)
@tag(['Contract'])
async def get_all_contracts():
    """
    Retrieves a list of all contracts.
    """
    contracts = await contract_service.get_all()
    response_data = ContractListResponseSchema(items=[ContractResponseSchema.model_validate(contract).model_dump() for contract in contracts])
    return response_data.model_dump()

@contract_bp.route('/contracts/<int:id>', methods=['PUT'])
@validate_request(ContractRequestSchema)
@validate_response(ContractResponseSchema)
@tag(['Contract'])
async def update_contract(id: int, data: ContractRequestSchema):
    """
    Updates a contract by its ID.
    """
    contract = await contract_service.update(id, **data.model_dump())
    if contract:
        response_data = ContractResponseSchema.model_validate(contract).model_dump()
        return response_data
    return jsonify({"error": "Contract not found"}), 404

@contract_bp.route('/contracts/<int:id>', methods=['DELETE'])
@tag(['Contract'])
async def delete_contract(id: int):
    """
    Deletes a contract by its ID.
    """
    success = await contract_service.delete(id)
    if success:
        return jsonify({"message": "Contract deleted successfully"})
    return jsonify({"error": "Contract not found"}), 404