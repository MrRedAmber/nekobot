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

        log.info('Databases: {0}\n Collections: {1}\n Files: {2}'.format(
            self.client.database_names(), self.db.collection_names(), self.collection.count()
        ))
        # TODO: REMOVE
        try:
            blogCol = self.collection.find()
            log.info('\n All data from the blog_data database \n')
            for blog in blogCol:
                log.info(blog)

        except Exception as e:
            print(str(e))
