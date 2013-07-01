""" 
    database handler for couchbase
"""
from couchbase import Couchbase

class CouchbaseHandler(object):
    """ encapselate the handler as a class """

    def __init__(self):
        """ instantiate the class vars """
        self.bucket = 'videos'
        self.client = Couchbase.connect(bucket=self.bucket)
