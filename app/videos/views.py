"""
    views file contains all the routes for the app and maps them to a
    specific hanlders function.
"""
from flask import Blueprint
from app.helpers.lazy_view import LazyView

videos = Blueprint('videos', __name__)

videos.add_url_rule('/', methods=['GET'], 
    view_func=LazyView('app.videos.handlers.get_videos'))
videos.add_url_rule('/<string:video_id>', methods=['GET'], 
    view_func=LazyView('app.videos.handlers.get_video'))
