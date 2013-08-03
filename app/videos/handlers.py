"""
    handlers file contains all the methods for the app views
"""
from flask import render_template, current_app
import json

user = { 'nickname': 'Chris' } # fake user

def get_videos():
    """ this example calls the Blueprint api.get_videos method and uses the
    data for the view """
    videos, code = current_app.view_functions['api_1.get_videos']()
    if code != 200:
        return render_template('404.html'), 404
    data = json.loads(videos.data)['data']
    print data
    return render_template("videos.html", title='videos', user=user, 
        videos=data)


def get_video(video_id):
    """ this example calls the Blueprint api.get_video method and uses the
    data for the view """
    video, code = current_app.view_functions['api_1.get_video'](video_id)
    data = json.loads(video.data)['data']
    if type(data) is not list:
        data = [data]
    return render_template("videos.html", title='videos', user=user, 
        videos=data)

