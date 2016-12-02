import logging

from lib.plugin import Plugin

log = logging.getLogger('discord')


class PluginManager:

    def __init__(self, nekobot):
        self.nekobot = nekobot
        self.nekobot.plugins = []

    def load(self, plugin):
        log.info('Loading plugin {}.'.format(plugin.__name__))
        plugin_instance = plugin(self.nekobot)
        self.nekobot.plugins.append(plugin_instance)
        log.info('Plugin {} loaded.'.format(plugin.__name__))

    def load_all(self):
        for plugin in Plugin.plugins:
            self.load(plugin)
