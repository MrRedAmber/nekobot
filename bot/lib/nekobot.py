import logging
import discord

from lib.plugin_manager import PluginManager
from lib.database import Database

log = logging.getLogger('discord')


class Nekobot(discord.Client):
    """
    Modified discord.Client to support plugins

    v0.1 Nekobot =^..^=
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.database = Database()
        self.plugin_manager = PluginManager(self)
        self.plugin_manager.load_all()

    async def get_channel_by_name(self, server, name):
        for channel in server.channels:
            if channel.name.lower() == name.lower():
                return {
                    'name': channel.name,
                    'obj': channel
                }
        return None

    # Get the commands in a list format
    async def get_commands(self):
        commands = []
        for plugin in self.plugins:
            command_list = await plugin.get_commands()
            if command_list is not None:
                commands.append(await plugin.get_commands())

        return commands

    # Called when the Client is ready
    async def on_ready(self):
        # Run each plugin's on ready
        for plugin in self.plugins:
            self.loop.create_task(plugin.on_ready())

        log.info('Nekobot is ready! =^..^=')

    # Called when a server is either created by the Client or when the Client
    # joins a server
    async def on_server_join(self, server):
        # Run each plugin's on server join
        for plugin in self.plugins:
            self.loop.create_task(plugin.on_server_join(server))

    # We don't want to bother with private messages
    async def on_message(self, message):
        if message.channel.is_private:
            return

        # Log the message inside the database
        self.database.log_message(message)

        # Run each plugin's on message
        for plugin in self.plugins:
            self.loop.create_task(plugin.on_message(message))
