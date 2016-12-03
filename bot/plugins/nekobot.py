import logging

from lib.decorators import channel_specific
from lib.plugin import Plugin

log = logging.getLogger('discord')

greetings = [
    'hey',
    'hello',
    'whats up',
    'what\'s up'
]


class Nekobot(Plugin):
    plugin_name = 'Nekobot'
    channel_name = 'nekobot'

    async def get_commands(self):
        commands = [
            {
                'name': '!whoareyou',
                'description': 'Ask Nekobot bot who she is'
            },
        ]
        return commands

    @channel_specific
    async def on_message(self, message, **kwargs):
        # Check for commands
        if message.content.startswith('!whoareyou'):
            await self.nekobot.send_message(
                message.channel,
                'I\'m a chat bot and I was born on December 1st 2016. \n'
                'My owner\'s name is Kaden but he likes to be called MrRedAmber.\n'
                'He isn\'t shy for constructive criticism and will is always\n'
                'open to take suggestions.\n\nMessage from MrRedAmber: \nI\'m'
                ' sorry if nekobot isn\'t working to well. She\'s still just a kitten \n'
                'and constantly learning about the brave new world around her!\n'
                'Check us out on github! https://github.com/MrRedAmber/nekobot.'
            )

        # Check if a greeting is in the message
        for greeting in greetings:
            if greeting in message.content:
                # Get a giphy using the giphy plugin
                gif = None
                for plugin in self.nekobot.plugins:
                    if plugin.plugin_name == 'Giphy':
                        gif = plugin.get_giphy('cat wink')

                # Check if the giphy function didn't return
                if gif is None:
                    return

                # Send a greeting back
                await self.nekobot.send_message(
                    message.channel,
                    'Hey there :3!\n{0}'.format(gif)
                )
                return
