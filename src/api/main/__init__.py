from quart import Blueprint, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
async def index():
    """
    Main route of the API.
    """
    return jsonify({"message": "Welcome to the Contracts API!"})