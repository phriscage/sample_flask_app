#!/usr/bin/python
"""
API bootstrap file
"""
from flask import Flask, jsonify, render_template
import sys
import os
import argparse
import logging
from couchbase import Couchbase
from couchbase.exceptions import ConnectError

#sys.path.insert(0, os.path.dirname(
    #os.path.realpath(__file__)) + '/../../../../lib')
#sys.path.insert(0, os.path.dirname(
    #os.path.realpath(__file__)) + '/../../../../conf')

#import sample
#from sampleconfig import Config

#if __name__ == "__main__":
    #sample.init_config(Config.get())

#logger = logging.getLogger('sample')

def connect_db():
    """ connect to couchbase """
    global db_client
    try:
        db_client = Couchbase.connect(host='127.0.0.1', port=8091, bucket='sample')
    except ConnectError as error:
        raise
    return db_client

db_client = connect_db()


def create_app():
    """ dynamically create the app """
    app = Flask(__name__, static_url_path='/static', static_folder='./static')
    app.config.from_object(__name__)

    #@app.teardown_appcontext
    #def shutdown_session(exception=None):
        #db_session.remove()

    #@app.errorhandler(400)
    @app.errorhandler(404)
    @app.errorhandler(405)
    @app.errorhandler(500)
    def default_error_handle(error=None):
        """ handle all errors with html output """
        return render_template('%s.html' % error.code), error.code

    ## add each api Blueprint and create the base route
    from core.views import core
    from videos.views import videos
    from maps.views import maps
    app.register_blueprint(core, url_prefix="/")
    app.register_blueprint(videos, url_prefix="/videos")
    app.register_blueprint(maps, url_prefix="/maps")
    #from sample.v1.api.core.views import core
    #app.register_blueprint(videos, url_prefix="/v1/videos")

    return app


def bootstrap(**kwargs):
    """bootstraps the application. can handle setup here"""
    app = create_app()
    app.debug = True
    app.run(host=kwargs['host'], port=kwargs['port'])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", help="Hostname or IP address",
        dest="host", type=str, default='0.0.0.0')
    parser.add_argument("--port", help="Port number",
        dest="port", type=int, default=8080)
    kwargs = parser.parse_args()
    bootstrap(**kwargs.__dict__)
