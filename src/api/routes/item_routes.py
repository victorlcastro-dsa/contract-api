from quart import Blueprint
from quart_schema import validate_request, validate_response, tag
from ..services import ItemService
from ..schemas import ItemRequestSchema, ItemResponseSchema, ItemListResponseSchema
from ..utils import ResponseHandler

item_bp = Blueprint('item', __name__)
item_service = ItemService()

@item_bp.route('/items', methods=['POST'])
@validate_request(ItemRequestSchema)
@validate_response(ItemResponseSchema, 201)
@tag(['Item'])
async def create_item(data: ItemRequestSchema):
    """
    Creates a new item with the provided data.
    """
    try:
        item = await item_service.create(data)
        response_data = ItemResponseSchema.model_validate(item).model_dump()
        return ResponseHandler.success(response_data)
    except Exception as e:
        return ResponseHandler.exception(e)

@item_bp.route('/items/<int:id>', methods=['GET'])
@validate_response(ItemResponseSchema)
@tag(['Item'])
async def get_item(id: int):
    """
    Retrieves an item by its ID.
    """
    try:
        item = await item_service.get_by_id(id)
        if item:
            response_data = ItemResponseSchema.model_validate(item).model_dump()
            return ResponseHandler.success(response_data)
        return ResponseHandler.error("Item not found", 404)
    except Exception as e:
        return ResponseHandler.exception(e)

@item_bp.route('/items', methods=['GET'])
@validate_response(ItemListResponseSchema)
@tag(['Item'])
async def get_all_items():
    """
    Retrieves a list of all items.
    """
    try:
        items = await item_service.get_all()
        response_data = ItemListResponseSchema(items=[ItemResponseSchema.model_validate(item).model_dump() for item in items])
        return ResponseHandler.success(response_data.model_dump())
    except Exception as e:
        return ResponseHandler.exception(e)

@item_bp.route('/items/<int:id>', methods=['PUT'])
@validate_request(ItemRequestSchema)
@validate_response(ItemResponseSchema)
@tag(['Item'])
async def update_item(id: int, data: ItemRequestSchema):
    """
    Updates an item by its ID.
    """
    try:
        item = await item_service.update(id, **data.model_dump())
        if item:
            response_data = ItemResponseSchema.model_validate(item).model_dump()
            return ResponseHandler.success(response_data)
        return ResponseHandler.error("Item not found", 404)
    except Exception as e:
        return ResponseHandler.exception(e)

@item_bp.route('/items/<int:id>', methods=['DELETE'])
@tag(['Item'])
async def delete_item(id: int):
    """
    Deletes an item by its ID.
    """
    try:
        success = await item_service.delete(id)
        if success:
            return ResponseHandler.success(message="Item deleted successfully")
        return ResponseHandler.error("Item not found", 404)
    except Exception as e:
        return ResponseHandler.exception(e)