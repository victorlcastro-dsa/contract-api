from quart import jsonify
from quart_schema import tag

@tag(["Main"])
async def index():
    """
    Main route of the API.
    """
    return jsonify({"message": "Welcome to the Contracts API!"})