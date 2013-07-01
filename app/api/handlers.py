import sys
import os
sys.path.insert(0, os.path.dirname(__file__) + '/../')

from database import CouchbaseHandler
from couchbase.exceptions import NotFoundError

from flask import render_template, jsonify, request, Blueprint
api = Blueprint('api', __name__)

client = CouchbaseHandler().client

## change all errors to json
@api.errorhandler(400)
@api.errorhandler(404)
@api.errorhandler(405)
#@api.errorhandler(500)
def default_error_handle(error=None):
    """ handle all errors with json output """
    return jsonify(error=error.code, message=error.message, success=False), \
        error.code


@api.route('/videos', methods = ['GET'])
def get_videos():
    try:
        videos = client.get_multi([str(v) for v in xrange(10)])
    except NotFoundError, error:
        #message = '%s: %s' % ('NotFoundError', error)
        message = "video '%s' does not exist." % error
        code = 404
        return jsonify(error=code, message=message, success=False), code
    return jsonify(data={ 'videos': videos }, success=True), 200


@api.route('/videos/<string:video_id>', methods = ['GET'])
def get_video(video_id):
    try:
        video = client.get(video_id)
        #video = filter(lambda t: t['id'] == video_id, videos)
    except NotFoundError, error:
        #message = '%s: %s' % ('NotFoundError', error)
        message = "video '%s' does not exist." % video_id
        code = 404
        return jsonify(error=code, message=message, success=False), code
    return jsonify(data={ video_id: video.value }, success=True), 200


@api.route('/add_numbers')
def get_add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

