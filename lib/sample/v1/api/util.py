"""API related utilities"""

from flask import make_response, request, current_app
from functools import update_wrapper

MAX_AGE = 21600


def crossdomain(origin=None, methods=None, headers=None,
                attach_to_all=True):
    """Allow cross-domain requests"""
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)

    def get_methods():
        """Get the applicable methods"""
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(func):
        """This function can be used as a decorator"""
        def wrapped_function(*args, **kwargs):
            """Wrapper"""
            if request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(func(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            resp.headers['Access-Control-Allow-Origin'] = origin
            resp.headers['Access-Control-Allow-Methods'] = get_methods()
            resp.headers['Access-Control-Max-Age'] = str(MAX_AGE)
            if headers is not None:
                resp.headers['Access-Control-Allow-Headers'] = headers
            return resp

        func.provide_automatic_options = False
        return update_wrapper(wrapped_function, func)
    return decorator
