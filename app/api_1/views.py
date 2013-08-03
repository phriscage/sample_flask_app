"""
    views file contains all the routes for the app and maps them to a
    specific hanlders function.
"""
from flask import jsonify, Blueprint
from handlers import get_video, get_videos, get_add_numbers

api_1 = Blueprint('api_1', __name__)

## change all errors to json
@api_1.errorhandler(400)
@api_1.errorhandler(404)
@api_1.errorhandler(405)
#@api_1.errorhandler(500)
def default_error_handle(error=None):
    """ handle all errors with json output """
    return jsonify(error=error.code, message=error.message, success=False), \
        error.code

api_1.add_url_rule('/videos', methods=['GET'], view_func=get_videos)
api_1.add_url_rule('/videos/<string:video_id>', methods=['GET'], 
    view_func=get_video)
api_1.add_url_rule('/add_numbers', methods=['GET'], view_func=get_add_numbers)
