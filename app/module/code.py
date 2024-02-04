from flask import current_app, Blueprint

# -- declare blueprint
module_bp = Blueprint('module', __name__, url_prefix='/module')


@module_bp.route('/')
def module_endpoint():
    return 'this is the module root endpoint'
