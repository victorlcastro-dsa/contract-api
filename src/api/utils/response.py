from quart import jsonify, request
from pydantic import ValidationError
import logging

logger = logging.getLogger(__name__)

class ResponseHandler:
    @staticmethod
    def success(data=None, message="Operação realizada com sucesso", status_code=200):
        response = {
            "status": "success",
            "message": message,
            "data": data
        }
        return jsonify(response), status_code

    @staticmethod
    def error(message="Ocorreu um erro", status_code=400, errors=None):
        response = {
            "status": "error",
            "message": message,
            "errors": errors
        }
        return jsonify(response), status_code

    @staticmethod
    def exception(exception, message="Exceção não tratada", status_code=500):
        logger.error(f"Exception: {exception}", exc_info=True)
        response = {
            "status": "fail",
            "message": message,
            "exception": str(exception)
        }
        return jsonify(response), status_code