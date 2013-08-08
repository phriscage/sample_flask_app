"""
    views file contains all the routes for the app and maps them to a 
    specific hanlders function.
"""
from app import app
from app.helpers.lazy_view import LazyView

app.add_url_rule('/favicon.ico', 
    view_func=LazyView('app.handlers.favicon'))
app.add_url_rule('/', methods=['GET'], 
    view_func=LazyView('app.handlers.index'))
app.add_url_rule('/index', methods=['GET'], 
    view_func=LazyView('app.handlers.index'))
app.add_url_rule('/add_numbers', 
    view_func=LazyView('app.handlers.add_numbers'))
