import logging


log = logging.getLogger('discord')


def channel_specific(function):

    """
        For limiting certain commands to specific channels

        if you implement this decorator you MUST set the
        channel_name variable in the plugin
    """

    async def wrapper(*args, **kwargs):
        # Check if the channel name is even set
        if args[0].channel_name is None:
            return

        #  Message channel name            Plugin channel name
        if args[1].channel.name.lower() != args[0].channel_name.lower():
            return

        return await function(*args, **kwargs)
    return wrapper


def permission_required(function):
    """
        Check if a given user has permissions to execute a certain command
    """
    async def wrapper(*args, **kwargs):
        # Parse out these values to make things a little bit easier for us
        message = args[1]
        author = message.author

        # Get the authors permissions
        permissions = {}
        for permission in author.server_permissions:
            permissions[permission[0]] = permission[1]

        # Check if the author has permission to execute the given command
        kwargs['has_permission'] = False

        if message.content.startswith('!ban'):
            kwargs['has_permission'] = permissions.get('ban_members')
        elif message.content.startswith('!kick'):
            kwargs['has_permission'] = permissions.get('kick_members')
        elif message.content.startswith('!whoisbanned'):
            kwargs['has_permission'] = permissions.get('kick_members')
        elif message.content.startswith('!unban'):
            kwargs['has_permission'] = permissions.get('kick_members')

        return await function(*args, **kwargs)
    return wrapper
