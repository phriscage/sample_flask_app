from flask import render_template, jsonify, request, current_app
from app import app
import json

user = { 'nickname': 'Chris' } # fake user

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template("index.html", title='Home', user=user)


@app.route('/videos', methods=['GET'])
def videos():
    """ this example calls the Blueprint api.get_videos method and uses the
    data for the view """
    videos, code = current_app.view_functions['api.get_videos']()
    if code != 200:
        return render_template('404.html'), 404
    data = json.loads(videos.data)['data']
    print data
    return render_template("videos.html", title='videos', user=user, 
        videos=data)


@app.route('/videos/<string:video_id>', methods=['GET'])
def video(video_id):
    """ this example calls the Blueprint api.get_video method and uses the
    data for the view """
    video, code = current_app.view_functions['api.get_video'](video_id)
    data = json.loads(video.data)['data']
    if type(data) is not list:
        data = [data]
    return render_template("videos.html", title='videos', user=user, 
        videos=data)


@app.route('/add_numbers')
def add_numbers():
    """ this example uses AJAX via JS to call the API """
    return render_template('add_numbers.html')
