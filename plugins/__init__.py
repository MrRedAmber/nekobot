from plugins import helloworld
import asyncio


def iter_plugins(client, message):
    helloworld.on_message(client, message)