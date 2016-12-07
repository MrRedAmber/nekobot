import logging
from lib.plugin import Plugin
import discord

log = logging.getLogger('discord')

greetings = [
    'hey',
    'hello',
    'whats up',
    'what\'s up'
]

who_are_you = 'Hey there! I\'m a chat bot and I was coded on December 1st 2016. \n' \
              'My developer\'s name is Kaden but he likes to be called MrRedAmber.\n' \
              'He isn\'t shy for constructive criticism and is always ' \
              'open to take suggestions.\n\nMessage from MrRedAmber: \nI\'m' \
              ' sorry if Nekobot isn\'t working to well. She\'s still just a kitten \n' \
              'and constantly learning about the brave new world around her!\n' \
              'Check us out on github! https://github.com/MrRedAmber/nekobot.'


class Nekobot(Plugin):
    plugin_name = 'nekobot-core'

    channels = [
        {
            'name': 'nekobot',
            'type': 'text',
            'private': False
        }
    ]

    async def get_commands(self):
        commands = [
            {
                'name': '!whoareyou',
                'description': 'Ask Nekobot bot who she is'
            },
        ]
        return commands

    async def on_message(self, message):
        # Limits the code to only executing in the nekobot channel
        if message.channel.name != 'nekobot':
            return

        # Command check
        if message.content.startswith('!whoareyou'):
            return await self.nekobot.send_message(
                message.channel,
                who_are_you
            )

        # Greeting check
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
                return await self.nekobot.send_message(
                    message.channel,
                    'Hey there :3!\n{0}'.format(gif)
                )


class Commands(Plugin):
    plugin_name = 'nekobot-commands'

    async def get_commands(self):
        commands = [
            {
                'name': '!commands',
                'description': 'Return a list of available commands'
            },
            {
                'name': '!plugins',
                'description': 'Return a list of enabled plugins'
            }
        ]
        return commands

    async def on_message(self, message):
        if message.content.startswith('!commands'):
            command_list = await self.nekobot.get_commands()

            crafted_message = 'Commands:\n\n'
            for plugin_commands in command_list:
                for command in plugin_commands:
                    crafted_message += '    {0}: {1}\n\n'.format(command['name'], command['description'])

            return await self.nekobot.send_message(
                message.channel,
                crafted_message
            )
        elif message.content.startswith('!plugins'):
            # plugins code
            plugin_names = []
            for plugin in self.nekobot.plugins:
                plugin_names.append(plugin.plugin_name)

            crafted_message = 'Plugins:\n\n'
            for plugin_name in plugin_names:
                crafted_message += '    [Enabled]: {0}\n\n'.format(plugin_name)

            return await self.nekobot.send_message(
                message.channel,
                crafted_message
            )
        else:
            return

# TODO: Works but needs to be cleaner
class Channels(Plugin):
    plugin_name = 'nekobot-channels'

    # Creates all the channels in plugins
    async def on_server_join(self, server):
        plugin_channels = []
        for plugin in self.nekobot.plugins:
            tmp_list = plugin.channels
            if tmp_list is not None:
                plugin_channels.append(tmp_list)

        for plugin_channel in plugin_channels:
            for channel in plugin_channel:
                log.info('CHANNEL INFORMATION: {0}'.format(channel))
                lf_channel = discord.utils.get(server.channels, name=channel['name'])

                if lf_channel is None:
                    await self.nekobot.create_channel(server, channel['name'], type=discord.ChannelType.text)
