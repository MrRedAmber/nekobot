from lib.plugin import Plugin
from lib.decorators import channel_specific
import logging

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

    @channel_specific
    async def on_message(self, message, **kwargs):
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
