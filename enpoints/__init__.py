from flask import Flask
import os
from flask_cors import CORS

config = {}

def create_app(app,cli=False):
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
    if os.getenv('FLASK_ENV') == 'development':
        app.config.from_object(config['development'])
    elif os.getenv('FLASK_ENV') == 'production':
        app.config.from_object(config['production'])
    else:
        app.config.from_object(config['default'])

    configure_extensions(app, cli)
    register_blueprints(app)


    if cli:
        print(app.config)

    return app


def configure_extensions(app, cli):
    app.config.update(config['extension_config'])
    db.init_app(app)
    if cli is True:
        migrate.init_app(app, db)
    jwt.init_app(app)
    if app.config['ENV'] == 'development':
        from flasgger import Swagger
        swagger = Swagger(app)  # TODO swagger config and api docs


def register_blueprints(app):
    app.register_blueprint(wx.views.bp)
    app.register_blueprint(api.views.bp)
    app.register_blueprint(operation.views.bp)
    app.register_blueprint(auth.views.bp)