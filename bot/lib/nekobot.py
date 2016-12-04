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

    async def create_nekobot_channel(self):
        # Find out if any of the connects servers don't have 'nekobot' in their channels
        server_list = []
        for server in self.servers:
            channel_list = []

            for channel in server.channels:
                channel_list.append(channel.name)

            if 'nekobot' not in channel_list:
                server_list.append(server)

        # Create the channel nekobot in the servers
        if server_list is None:
            return

        # Iterate through all of the servers
        for server in server_list:
            # Create the channel
            await self.create_channel(server, 'nekobot')

    async def get_commands(self):
        commands = []
        for plugin in self.plugins:
            command_list = await plugin.get_commands()
            if command_list is not None:
                commands.append(await plugin.get_commands())

        return commands

    async def on_ready(self):
        # Called when the bot is ready
        await self.create_nekobot_channel()
        log.info('Nekobot is ready! =^..^=')

    async def on_server_join(self, server):
        pass

    async def on_message(self, message):
        if message.channel.is_private:
            return

        for plugin in self.plugins:
            self.loop.create_task(plugin.on_message(message))

