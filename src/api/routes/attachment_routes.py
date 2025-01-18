from quart import Blueprint, request, jsonify
from quart_schema import validate_request, validate_response
from ..services import AttachmentService
from ..schemas import AttachmentRequestSchema, AttachmentResponseSchema, AttachmentListResponseSchema

attachment_bp = Blueprint('attachment', __name__)
attachment_service = AttachmentService()

@attachment_bp.route('/attachments', methods=['POST'])
@validate_request(AttachmentRequestSchema)
@validate_response(AttachmentResponseSchema, 201)
async def create_attachment(data: AttachmentRequestSchema):
    attachment = await attachment_service.create(data)
    return jsonify(attachment)

@attachment_bp.route('/attachments/<int:id>', methods=['GET'])
@validate_response(AttachmentResponseSchema)
async def get_attachment(id: int):
    attachment = await attachment_service.get_by_id(id)
    if attachment:
        return jsonify(attachment)
    return jsonify({"error": "Attachment not found"}), 404

@attachment_bp.route('/attachments', methods=['GET'])
@validate_response(AttachmentListResponseSchema)
async def get_all_attachments():
    attachments = await attachment_service.get_all()
    return jsonify(attachments)

@attachment_bp.route('/attachments/<int:id>', methods=['PUT'])
@validate_request(AttachmentRequestSchema)
@validate_response(AttachmentResponseSchema)
async def update_attachment(id: int, data: AttachmentRequestSchema):
    attachment = await attachment_service.update(id, **data.model_dump())
    if attachment:
        return jsonify(attachment)
    return jsonify({"error": "Attachment not found"}), 404

@attachment_bp.route('/attachments/<int:id>', methods=['DELETE'])
async def delete_attachment(id: int):
    success = await attachment_service.delete(id)
    if success:
        return jsonify({"message": "Attachment deleted successfully"})
    return jsonify({"error": "Attachment not found"}), 404