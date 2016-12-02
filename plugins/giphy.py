from lib.plugin import Plugin
from random import randrange
import logging
import re
import requests

log = logging.getLogger('discord')


class Giphy(Plugin):
    plugin_name = 'Giphy'

    async def get_commands(self):
        commands = [
            {
                'name': '!gif keyword',
                'description': 'Search the Giphy collection '
                               'against a given keyword'
            },
            {
                'name': '!giphy keyword',
                'description': 'Search the Giphy collection '
                               'against a given keyword'
            }
        ]
        return commands

    def get_giphy(self, keyword):
        try:
            data = requests.get('http://api.giphy.com/v1/gifs/search?q='
                                    + keyword.replace(' ', '+')
                                    + '&api_key=dc6zaTOxFJmzC').json()

            return data['data'][randrange(len(data['data']))] \
                ['images']['original']['url']
        except Exception as e:
            print(e.args)
            return 'Giphy encountered an error :cry: ...'

    async def on_message(self, message):

        rule = r'!(gif|giphy) (.*)'
        check = re.match(rule, message.content)

        if check is None:
            return

        # log.info('{}#{}@{} >> {}'.format(
        #     message.author.name,
        #     message.author.discriminator,
        #     message.server.name,
        #     message.clean_content
        # ))

        nature, name = check.groups()
        gif = self.get_giphy(name)
        print(gif)
        if gif == '' or gif is None:
            await self.nekobot.send_message(
                message.channel,
                'I didn\'t find anything :cry: ...'
            )
            return

        await self.nekobot.send_message(
            message.channel,
            'What a magificent gif! \n' + gif
        )