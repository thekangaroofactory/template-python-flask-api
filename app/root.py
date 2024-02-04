from flask import current_app, Blueprint

# -- declare blueprint
root_bp = Blueprint('root', __name__)


@root_bp.route('/')
def root_endpoint():
    return 'this is the root endpoint of the API, docs should go here.'
