# project/server/__init__.py

import logging
import traceback
import sys
from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from flask_swagger import swagger
from flask_bootstrap import Bootstrap
from loguru import logger


# create a custom handler
class InterceptHandler(logging.Handler):
    def emit(self, record):
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(record.levelno, record.getMessage())


def create_app(script_info=None):

    # instantiate the app
    app = Flask(
        __name__,
        static_folder='./static',
    )
    Bootstrap(app)
    handler = InterceptHandler()
    handler.setLevel(0)
    app.logger.addHandler(handler)

    # from src.controller import blueprint


    SWAGGER_URL = '/api/docs'
    API_URL = '/api/swagger.json'

    swaggerui_blueprint = get_swaggerui_blueprint(
        # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
        SWAGGER_URL,
        API_URL,
        config={  # Swagger UI config overrides
            'app_name': "PublicOpinionAlert API"
        }
    )

    app.register_blueprint(swaggerui_blueprint)

    @app.route(API_URL)
    def spec():
        return jsonify(swagger(app))

    @app.errorhandler(Exception)
    def global_error_handle(error):
        trace = traceback.format_exc()
        status_code = getattr(error, 'status_code', 400)
        response_dict = dict(getattr(error, 'payload', None) or ())
        response_dict['message'] = str(error)
        response_dict['traceback'] = trace
        response = jsonify(response_dict)
        response.status_code = status_code
        traceback.print_exc(file=sys.stdout)
        return response
    return app
