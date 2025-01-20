from quart import Blueprint
from quart_schema import tag
from ..utils import ResponseHandler

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
@tag(["Main"])
async def index():
    """
    Main route of the API.
    """
    try:
        return ResponseHandler.success(message="Welcome to the Contracts API!")
    except Exception as e:
        return ResponseHandler.exception(e)