from quart import Blueprint
from quart_schema import validate_request, validate_response, tag
from ..services import ContractService
from ..schemas import ContractRequestSchema, ContractResponseSchema, ContractListResponseSchema
from ..utils import ResponseHandler

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
    try:
        contract = await contract_service.create(data)
        response_data = ContractResponseSchema.model_validate(contract).model_dump()
        return ResponseHandler.success(response_data)
    except Exception as e:
        return ResponseHandler.exception(e)

@contract_bp.route('/contracts/<int:id>', methods=['GET'])
@validate_response(ContractResponseSchema)
@tag(['Contract'])
async def get_contract(id: int):
    """
    Retrieves a contract by its ID.
    """
    try:
        contract = await contract_service.get_by_id(id)
        if contract:
            response_data = ContractResponseSchema.model_validate(contract).model_dump()
            return ResponseHandler.success(response_data)
        return ResponseHandler.error("Contract not found", 404)
    except Exception as e:
        return ResponseHandler.exception(e)

@contract_bp.route('/contracts', methods=['GET'])
@validate_response(ContractListResponseSchema)
@tag(['Contract'])
async def get_all_contracts():
    """
    Retrieves a list of all contracts.
    """
    try:
        contracts = await contract_service.get_all()
        response_data = ContractListResponseSchema(items=[ContractResponseSchema.model_validate(contract).model_dump() for contract in contracts])
        return ResponseHandler.success(response_data.model_dump())
    except Exception as e:
        return ResponseHandler.exception(e)

@contract_bp.route('/contracts/<int:id>', methods=['PUT'])
@validate_request(ContractRequestSchema)
@validate_response(ContractResponseSchema)
@tag(['Contract'])
async def update_contract(id: int, data: ContractRequestSchema):
    """
    Updates a contract by its ID.
    """
    try:
        contract = await contract_service.update(id, **data.model_dump())
        if contract:
            response_data = ContractResponseSchema.model_validate(contract).model_dump()
            return ResponseHandler.success(response_data)
        return ResponseHandler.error("Contract not found", 404)
    except Exception as e:
        return ResponseHandler.exception(e)

@contract_bp.route('/contracts/<int:id>', methods=['DELETE'])
@tag(['Contract'])
async def delete_contract(id: int):
    """
    Deletes a contract by its ID.
    """
    try:
        success = await contract_service.delete(id)
        if success:
            return ResponseHandler.success(message="Contract deleted successfully")
        return ResponseHandler.error("Contract not found", 404)
    except Exception as e:
        return ResponseHandler.exception(e)