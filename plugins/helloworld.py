from lib.plugin import Plugin


class HelloWorld(Plugin):
    plugin_name = 'HelloWorld!'

    async def get_commands(self, server):
        commands = [
            {
                'name': '!hw',
                'description': 'Gives you information about an animu.'
            }
        ]
        return commands

    async def on_message(self, message):
        if message.content.startswith('!hw'):
            await self.nekobot.send_message(message.channel, 'Hello World!')