from lib.plugin import Plugin
from lib.decorators import auth_required
from discord.errors import Forbidden
import logging


log = logging.getLogger('discord')


class Moderator(Plugin):
    plugin_name = 'Moderator'

    async def get_commands(self):
        commands = [
            {
                'name': '!ban <username>'
            }
        ]
        pass

    @auth_required
    async def on_message(self, message, has_permission):
        # Check if the user has the permissions to execute the following actions
        if not has_permission:
            raise Forbidden

        try:
            # is ban command?
            if message.content.startswith('!ban'):
                # for each person in mentions, ban
                for mention in message.mentions:
                    await self.nekobot.ban(mention)

                    await self.nekobot.send_message(
                        message.channel,
                        'Successfully banned: {0}'.format(mention)
                    )

            # is kick command?
            elif message.content.startswith('!kick'):
                # for each person in mentions, kick
                for mention in message.mentions:
                    await self.nekobot.kick(mention)

                    await self.nekobot.send_message(
                        message.channel,
                        'Successfully kicked: {0}'.format(mention)
                    )
        except Forbidden as e:
            await self.nekobot.send_message(
                message.channel,
                'You don\'t have permission to execute that command :cry:...'
            )

            log.info('ERROR ERROR ERROR: {0}'.format(str(e)))
