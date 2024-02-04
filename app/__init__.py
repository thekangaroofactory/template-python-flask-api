from flask import Flask


def create_app():
    # -- create api
    app = Flask(__name__)
    app.config.from_pyfile("../config.py")

    # -- db object should be defined within a model module, then imported here for init
    # from yourapplication.model import db
    # db.init_app(app)

    # -- declare blueprints
    # note that blueprints should use current_app since they can't import app
    from app.module.code import module_bp
    app.register_blueprint(module_bp)

    from app.root import root_bp
    app.register_blueprint(root_bp)

    return app
