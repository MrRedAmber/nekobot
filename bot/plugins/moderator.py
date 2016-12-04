from lib.plugin import Plugin
from lib.decorators import permission_required
from discord.errors import Forbidden, HTTPException
from aiohttp import ClientResponse
import logging


log = logging.getLogger('discord')


class Moderator(Plugin):
    plugin_name = 'Moderator'
    channel_id = None

    async def get_commands(self):
        commands = [
            {
                'name': '!ban <username_mention>',
                'description': 'bans a user from the discord server'
            },
            {
                'name': '!kick <username_mention>',
                'description': 'kicks a user from the discord server'
            },
            {
                'name': '!whoisbanned',
                'description': 'get a list of banned users'
            },
            {
                'name': '!unban',
                'description': 'Unbanned a user by their used id'
            }
        ]
        return commands

    @permission_required
    async def on_message(self, message, has_permission):
        # Check if the user has the permissions to execute the following actions
        if not has_permission:
            return

        channel_list = self.nekobot.get_all_channels()
        for channel in channel_list:
            if channel.name == 'nekobot':
                self.channel_id = channel.id

        try:
            # Ban Command
            if message.content.startswith('!ban'):
                # for each person in mentions, ban
                for mention in message.mentions:
                    await self.nekobot.ban(mention)

                    await self.nekobot.send_message(
                        self.nekobot.get_channel(self.channel_id),
                        'Successfully banned: {0}.'.format(mention)
                    )

            # Kick Command
            elif message.content.startswith('!kick'):
                # for each person in mentions, kick
                for mention in message.mentions:
                    await self.nekobot.kick(mention)

                    await self.nekobot.send_message(
                        self.nekobot.get_channel(self.channel_id),
                        'Successfully kicked: {0}.'.format(mention)
                    )
            elif message.content.startswith('!whoisbanned'):
                banned = await self.nekobot.get_bans(message.server)
                msg_str = 'Banned users:\n\n'

                for banned_user in banned:
                    msg_str += '    Name: {0} \n    ID: {1}\n\n'.format(banned_user.name, banned_user.id)

                await self.nekobot.send_message(
                    self.nekobot.get_channel(self.channel_id),
                    msg_str
                )

            elif message.content.startswith('!unban'):
                user_id = message.content.split(' ')[1]
                banned_user = await self.nekobot.get_user_info(user_id)
                await self.nekobot.unban(message.server, banned_user)

                await self.nekobot.send_message(
                    self.nekobot.get_channel(self.channel_id),
                    'Successfully unbanned user: {0}'.format(banned_user.name)
                )

        except Forbidden as e:
            await self.nekobot.send_message(
                self.nekobot.get_channel(self.channel_id),
                'You don\'t have permission to execute that command :cry:...'
            )
        except HTTPException as e:
            await self.nekobot.send_message(
                self.nekobot.get_channel(self.channel_id),
                'An error occurred trying to execute that command! :cry:'
            )