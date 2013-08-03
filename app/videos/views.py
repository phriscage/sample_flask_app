"""
    views file contains all the routes for the app and maps them to a
    specific hanlders function.
"""
from flask import Blueprint
from handlers import get_video, get_videos

videos = Blueprint('videos', __name__)

videos.add_url_rule('/', methods=['GET'], view_func=get_videos)
videos.add_url_rule('/<string:video_id>', methods=['GET'], view_func=get_video)
