#!/usr/bin/env python3
"""TradeHub Flask Application
"""
import os
from flask import Flask, jsonify, render_template, make_response
from models.engine.db import DB
from flask_cors import CORS
from flasgger import Swagger
from api.v1.views import app_views
from api.v1.auth import auth


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

app.register_blueprint(app_views)
app.register_blueprint(auth)

cors = CORS(app, resources={r'api/v1/*': {'origins': '*'}})


@app.teardown_appcontext
def close_db(error):
    """Close Database
    """
    DB.close()

@app.errorhandler(404)
def page_not_found(error):
    """404 Error
    ---
    responses:
        404:
            description: resource not found
    """
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(500)
def internal_error(error):
    """500 Error
    ---
    responses:
        500:
            description: Internal serval error
    """
    return make_response(jsonify({'error': 'Internal server error'}), 500)

app.config['SWAGGER'] = {
        'title': 'TradeHub RESTful API',
        'version': 1.0
}
Swagger(app)


if __name__ == '__main__':
    """Main function
    """
    host = os.getenv('TRADEHUB_API_HOST')
    port = os.getenv('TRADEHUB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'

    app.run(host=host, port=port, debug=True)
