from flask import Blueprint, redirect, url_for, render_template, jsonify

videos = Blueprint('videos', __name__, template_folder='templates')

@videos.route('', methods=['GET'])
def get_index():
    """ root path to index """
    return render_template('videos/index.html') 
