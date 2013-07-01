#!/usr/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

videos = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

## change all errors to json
@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(405)
@app.errorhandler(500)
def default_error_handle(error=None):
    """ handle all errors with json output """
    return jsonify(error=error.code, message=error.message, success=False), \
        error.code

## routes
#@app.route('/')
#def index():
    #""" default root index """
    #return render_template('index.html', docs_url=docs_url)

@app.route('/api/1/videos', methods = ['GET'])
def get_videos():
   	return jsonify(data={ 'videos': videos }, success=True)

@app.route('/api/1/videos/<int:video_id>', methods = ['GET'])
def get_video(video_id):
    video = filter(lambda t: t['id'] == video_id, videos)
    if len(video) == 0:
        message = "video '%i' does not exist." % video_id
        code = 404
        return jsonify(error=code, message=message, success=False), code
    return jsonify(data={ 'video': video[0] }, success=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)

