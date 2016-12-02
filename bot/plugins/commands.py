import logging

from lib.plugin import Plugin

log = logging.getLogger('discord')


class Commands(Plugin):
    plugin_name = 'Commands'

    async def get_commands(self):
        commands = [
            {
                'name': '!commands',
                'description': 'Return a list of available commands'
            }
        ]
        return commands

    async def on_message(self, message):
        if not message.content.startswith('!commands'):
            return

        command_list = await self.nekobot.get_commands()

        crafted_message = 'Commands:\n\n'
        for plugin_commands in command_list:
            for command in plugin_commands:
                crafted_message += '    {0}: {1}\n\n'.format(command['name'], command['description'])

        await self.nekobot.send_message(
            message.channel,
            crafted_message
        )

