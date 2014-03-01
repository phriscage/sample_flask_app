"""
    LazyView helper to only load view functions as needed and imports the real
    function on first use. 
    What's important here is is that __module__ and __name__ are properly set. 
    This is used by Flask internally to figure out how to name the URL rules in 
    case you don't provide a name for the rule yourself.
    http://flask.pocoo.org/docs/patterns/lazyloading/
"""

from werkzeug import import_string, cached_property

class LazyView(object):

    def __init__(self, import_name):
        self.__module__, self.__name__ = import_name.rsplit('.', 1)
        self.import_name = import_name

    @cached_property
    def view(self):
        return import_string(self.import_name)

    def __call__(self, *args, **kwargs):
        return self.view(*args, **kwargs)

