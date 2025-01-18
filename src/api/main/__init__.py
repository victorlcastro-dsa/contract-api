from quart import Blueprint, jsonify
from quart_schema import tag

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
@tag(["Main"])
async def index():
    """
    Main route of the API.
    """
    return jsonify({"message": "Welcome to the Contracts API!"})