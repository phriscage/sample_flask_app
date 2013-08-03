"""
    handlers file contains all the methods for the app views
"""
import os
from flask import render_template, send_from_directory
from app import app

user = { 'nickname': 'Chris' } # fake user

def index():
    return render_template("index.html", title='Home', user=user)

def add_numbers():
    """ this example uses AJAX via JS to call the API """
    return render_template('add_numbers.html')

def favicon():
    """ default favicon method """
    return send_from_directory(os.path.join(app.root_path, 'static'),
               'favicon.ico', mimetype='image/vnd.microsoft.icon')
