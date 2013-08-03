""" 
    main flask app that instantiates all the blueprints and routes
"""
from flask import Flask

app = Flask(__name__)

from app import views
from app.videos.views import videos
from app.api_1.views import api_1
app.register_blueprint(videos, url_prefix="/videos")
app.register_blueprint(api_1, url_prefix="/api/1")
