from quart import Blueprint, request, jsonify
from quart_schema import validate_request, validate_response, tag
from ..services import AttachmentService
from ..schemas import AttachmentRequestSchema, AttachmentResponseSchema, AttachmentListResponseSchema

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
    attachment = await attachment_service.create(data)
    response_data = AttachmentResponseSchema.model_validate(attachment).model_dump()
    return jsonify(response_data)

@attachment_bp.route('/attachments/<int:id>', methods=['GET'])
@validate_response(AttachmentResponseSchema)
@tag(['Attachment'])
async def get_attachment(id: int):
    """
    Retrieves an attachment by its ID.
    """
    attachment = await attachment_service.get_by_id(id)
    if attachment:
        response_data = AttachmentResponseSchema.model_validate(attachment).model_dump()
        return response_data
    return jsonify({"error": "Attachment not found"}), 404

@attachment_bp.route('/attachments', methods=['GET'])
@validate_response(AttachmentListResponseSchema)
@tag(['Attachment'])
async def get_all_attachments():
    """
    Retrieves a list of all attachments.
    """
    attachments = await attachment_service.get_all()
    response_data = AttachmentListResponseSchema(items=[AttachmentResponseSchema.model_validate(attachment).model_dump() for attachment in attachments])
    return response_data.model_dump()

@attachment_bp.route('/attachments/<int:id>', methods=['PUT'])
@validate_request(AttachmentRequestSchema)
@validate_response(AttachmentResponseSchema)
@tag(['Attachment'])
async def update_attachment(id: int, data: AttachmentRequestSchema):
    """
    Updates an attachment by its ID.
    """
    attachment = await attachment_service.update(id, **data.model_dump())
    if attachment:
        response_data = AttachmentResponseSchema.model_validate(attachment).model_dump()
        return response_data
    return jsonify({"error": "Attachment not found"}), 404

@attachment_bp.route('/attachments/<int:id>', methods=['DELETE'])
@tag(['Attachment'])
async def delete_attachment(id: int):
    """
    Deletes an attachment by its ID.
    """
    success = await attachment_service.delete(id)
    if success:
        return jsonify({"message": "Attachment deleted successfully"})
    return jsonify({"error": "Attachment not found"}), 404