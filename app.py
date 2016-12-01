import logging
import os

from lib.nekobot import Nekobot

# Load the plugins
from plugins.helloworld import HelloWorld
from plugins.giphy import Giphy

# Load the Nekobot environment
with open('nekobot.rc', 'r') as nekobotrc:
    for line in nekobotrc:
        export = line.split('=')
        os.environ[export[0]] = export[1].strip('\n')

nekobotrc.close()
# Finish loading the Nekobot environment

# Setup the logging system
logger = logging.getLogger('discord')
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

if os.environ['nekobot_debug']:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)
# Finish setting up the login system

# Start the Nekobot
bot = Nekobot()
bot.run(os.environ['nekobot_token'])
