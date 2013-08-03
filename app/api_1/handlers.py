"""
    handlers file contains all the methods for the app views
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__) + '/../')

from flask import jsonify, request
from database import CouchbaseHandler
from couchbase.exceptions import NotFoundError

client = CouchbaseHandler().client

def get_videos():
    """ this method uses the couchbase client and get multi for a range of
    keys """
    try:
        videos = client.get_multi([str(v) for v in xrange(10)])
    except NotFoundError, error:
        #message = '%s: %s' % ('NotFoundError', error)
        message = "video '%s' does not exist." % error
        code = 404
        return jsonify(error=code, message=message, success=False), code
    return jsonify(data={ 'videos': videos }, success=True), 200


def get_video(video_id):
    """ this method uses the couchbase client and gets the key value or returns
    an error """
    try:
        video = client.get(video_id)
        #video = filter(lambda t: t['id'] == video_id, videos)
    except NotFoundError, error:
        #message = '%s: %s' % ('NotFoundError', error)
        message = "video '%s' does not exist." % video_id
        code = 404
        return jsonify(error=code, message=message, success=False), code
    return jsonify(data={ video_id: video.value }, success=True), 200


def get_add_numbers():
    """ test method to return addition of two numbers """
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

