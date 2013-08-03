"""
    views file contains all the routes for the app and maps them to a 
    specific hanlders function.
"""
from flask import render_template
from app import app
from handlers import index, add_numbers, favicon

app.add_url_rule('/favicon.ico', view_func=favicon)
app.add_url_rule('/', methods=['GET'], view_func=index)
app.add_url_rule('/index', methods=['GET'], view_func=index)
app.add_url_rule('/add_numbers', view_func=add_numbers)
