from pymongo import MongoClient
import logging
import datetime

log = logging.getLogger('discord')


class Database:
    def __init__(self):
        # Get the client handle from MongoDB
        self.client = MongoClient('mongodb://mongodb:27017/')

        # Get a database from the client handle
        self.db = self.client['blog_data']

        # Get collection from the database handle
        self.collection = self.db['blog_post']

