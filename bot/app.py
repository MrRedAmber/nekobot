import logging, os

from lib.nekobot import Nekobot

# Load the plugins

from plugins import commands
from plugins import giphy
from plugins import nekobot
from plugins import moderator

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
