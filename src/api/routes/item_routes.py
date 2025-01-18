from quart import Blueprint, request, jsonify
from quart_schema import validate_request, validate_response
from ..services import ItemService
from ..schemas import ItemRequestSchema, ItemResponseSchema, ItemListResponseSchema

item_bp = Blueprint('item', __name__)
item_service = ItemService()

@item_bp.route('/items', methods=['POST'])
@validate_request(ItemRequestSchema)
@validate_response(ItemResponseSchema, 201)
async def create_item(data: ItemRequestSchema):
    item = await item_service.create(data)
    return jsonify(item)

@item_bp.route('/items/<int:id>', methods=['GET'])
@validate_response(ItemResponseSchema)
async def get_item(id: int):
    item = await item_service.get_by_id(id)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

@item_bp.route('/items', methods=['GET'])
@validate_response(ItemListResponseSchema)
async def get_all_items():
    items = await item_service.get_all()
    return jsonify(items)

@item_bp.route('/items/<int:id>', methods=['PUT'])
@validate_request(ItemRequestSchema)
@validate_response(ItemResponseSchema)
async def update_item(id: int, data: ItemRequestSchema):
    item = await item_service.update(id, **data.model_dump())
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

@item_bp.route('/items/<int:id>', methods=['DELETE'])
async def delete_item(id: int):
    success = await item_service.delete(id)
    if success:
        return jsonify({"message": "Item deleted successfully"})
    return jsonify({"error": "Item not found"}), 404