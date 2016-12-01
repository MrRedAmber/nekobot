from lib.plugin_manager import PluginManager
import logging
import discord

log = logging.getLogger('discord')


class Nekobot(discord.Client):
    """
    Modified discord.Client to support plugins

    v1.0 Nekobot =^..^=

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.plugin_manager = PluginManager(self)
        self.plugin_manager.load_all()

    async def on_ready(self):
        # Called when the bot is ready
        log.info('Nekobot is ready! =^..^=')

    async def send_message(self, *args, **kwargs):
        return await super().send_message(*args, **kwargs)

    async def on_message(self, message):
        if message.channel.is_private:
            return

        for plugin in self.plugins:
            self.loop.create_task(plugin.on_message(message))

