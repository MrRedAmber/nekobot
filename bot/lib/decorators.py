import logging


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

