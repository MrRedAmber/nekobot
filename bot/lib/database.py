from pymongo import MongoClient
from datetime import datetime
import logging

log = logging.getLogger('discord')


class Database:
    """
    A class for interfacing with the mongodb container
    """
    def __init__(self):
        # Get the client/database handle from mongodb container
        self.client = MongoClient('mongodb://mongodb:27017/')

        # Create the message log database
        self.message_log = self.client['message_log']

    def log_message(self, message):
        # This is all of the content I really care about right now
        self.message_log[message.server.name].insert_one({
            'author': message.author.name,
            'discriminator': message.author.discriminator,
            'clean_content': message.clean_content,
            'timestamp': datetime.utcnow()
        })
