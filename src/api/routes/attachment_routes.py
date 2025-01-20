from quart import Blueprint
from quart_schema import validate_request, validate_response, tag
from ..services import AttachmentService
from ..schemas import AttachmentRequestSchema, AttachmentResponseSchema, AttachmentListResponseSchema
from ..utils import ResponseHandler

attachment_bp = Blueprint('attachment', __name__)
attachment_service = AttachmentService()

@attachment_bp.route('/attachments', methods=['POST'])
@validate_request(AttachmentRequestSchema)
@validate_response(AttachmentResponseSchema, 201)
@tag(['Attachment'])
async def create_attachment(data: AttachmentRequestSchema):
    """
    Creates a new attachment with the provided data.
    """
    try:
        attachment = await attachment_service.create(data)
        response_data = AttachmentResponseSchema.model_validate(attachment).model_dump()
        return ResponseHandler.success(response_data)
    except Exception as e:
        return ResponseHandler.exception(e)

@attachment_bp.route('/attachments/<int:id>', methods=['GET'])
@validate_response(AttachmentResponseSchema)
@tag(['Attachment'])
async def get_attachment(id: int):
    """
    Retrieves an attachment by its ID.
    """
    try:
        attachment = await attachment_service.get_by_id(id)
        if attachment:
            response_data = AttachmentResponseSchema.model_validate(attachment).model_dump()
            return ResponseHandler.success(response_data)
        return ResponseHandler.error("Attachment not found", 404)
    except Exception as e:
        return ResponseHandler.exception(e)

@attachment_bp.route('/attachments', methods=['GET'])
@validate_response(AttachmentListResponseSchema)
@tag(['Attachment'])
async def get_all_attachments():
    """
    Retrieves a list of all attachments.
    """
    try:
        attachments = await attachment_service.get_all()
        response_data = AttachmentListResponseSchema(items=[AttachmentResponseSchema.model_validate(attachment).model_dump() for attachment in attachments])
        return ResponseHandler.success(response_data.model_dump())
    except Exception as e:
        return ResponseHandler.exception(e)

@attachment_bp.route('/attachments/<int:id>', methods=['PUT'])
@validate_request(AttachmentRequestSchema)
@validate_response(AttachmentResponseSchema)
@tag(['Attachment'])
async def update_attachment(id: int, data: AttachmentRequestSchema):
    """
    Updates an attachment by its ID.
    """
    try:
        attachment = await attachment_service.update(id, **data.model_dump())
        if attachment:
            response_data = AttachmentResponseSchema.model_validate(attachment).model_dump()
            return ResponseHandler.success(response_data)
        return ResponseHandler.error("Attachment not found", 404)
    except Exception as e:
        return ResponseHandler.exception(e)

@attachment_bp.route('/attachments/<int:id>', methods=['DELETE'])
@tag(['Attachment'])
async def delete_attachment(id: int):
    """
    Deletes an attachment by its ID.
    """
    try:
        success = await attachment_service.delete(id)
        if success:
            return ResponseHandler.success(message="Attachment deleted successfully")
        return ResponseHandler.error("Attachment not found", 404)
    except Exception as e:
        return ResponseHandler.exception(e)