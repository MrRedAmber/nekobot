import logging
import re
from random import randrange
import requests
import aiohttp


from lib.plugin import Plugin

log = logging.getLogger('discord')


class Giphy(Plugin):
    plugin_name = 'Giphy'

    async def get_commands(self):
        commands = [
            {
                'name': '!gif <keyword>',
                'description': 'Search the Giphy collection '
                               'against a given keyword'
            },
            {
                'name': '!giphy <keyword>',
                'description': 'Search the Giphy collection '
                               'against a given keyword'
            }
        ]
        return commands

    async def get_giphy(self, keyword):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get('http://api.giphy.com/v1/gifs/search?q='
                                       + keyword.replace(' ','+')
                                       + '&api_key=dc6zaTOxFJmzC') as resp:

                    if resp.status == 200:
                        response_json = await resp.json()
                        url = response_json.get('data')\
                              [randrange(len(response_json.get('data')))]\
                              .get('images')\
                              .get('original')\
                              .get('url')

                        return url

                    return 'Giphy encountered an error :cry: ...'

            except Exception as e:
                log.info("Cannot get gif from giphy api using keyword: {}".format(keyword))
                log.info(e)
                return 'Giphy encountered an error :cry: ...'

    async def on_message(self, message):

        rule = r'!(gif|giphy) (.*)'
        check = re.match(rule, message.content)

        if check is None:
            return

        nature, name = check.groups()
        gif = await self.get_giphy(name)

        if gif == '' or gif is None:
            await self.nekobot.send_message(
                message.channel,
                'I didn\'t find anything :cry: ...'
            )
            return

        await self.nekobot.send_message(
            message.channel,
            gif
        )