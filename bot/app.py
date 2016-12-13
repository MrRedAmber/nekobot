# Import the modified client
from lib.nekobot import Nekobot

# Python level imports
import importlib
import os
import logging

# Load the plugins

for file in os.listdir('./plugins'):
    importlib.import_module('plugins.' + file.split('.py')[0])

# Finish loading the plugins

# Setup the logging system

logger = logging.getLogger('discord')
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

if os.environ['NEKOBOT_DEBUG']:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)
# Finish setting up the login system

# Start the Nekobot
bot = Nekobot()
bot.run(os.environ['NEKOBOT_TOKEN'])
