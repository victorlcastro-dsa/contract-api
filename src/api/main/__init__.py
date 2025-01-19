from quart import Blueprint
from .routes import index

main_bp = Blueprint('main', __name__)

# Registrar as rotas
main_bp.add_url_rule('/', view_func=index)