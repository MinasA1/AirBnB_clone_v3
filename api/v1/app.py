#!/usr/bin/env python3
"""api app"""
from sys import path
path.insert(0, "../")
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify
from os import getenv


app = Flask('api')
app.url_map.strict_slashes = False
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    """call storage.close()"""
    storage.close()


@app.errorhandler(404)
def error_404(error):
    """handles 404 error"""
    return jsonify({'error': 'Not found'}), 404

if __name__ == "__main__":
    app.run(host=getenv('HBNB_API_HOST', default='0.0.0.0'),
            port=getenv('HBNB_API_PORT', default=5000))
