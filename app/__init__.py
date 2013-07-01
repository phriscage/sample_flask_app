from flask import Flask, jsonify

app = Flask(__name__)

from app import views
from app.api.handlers import api
app.register_blueprint(api, url_prefix="/api/1")
