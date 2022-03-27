from os import environ

from discord import Client, DMChannel
from replit import db

from messages import display_help, ode_of_monty
from form import get_user_data
from connect import make_connections
from person import Person

# Setup
DISCORD_TOKEN = environ['TOKEN']

client = Client()


@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith("!monty python"):
        await ode_of_monty(message)
        return

    if message.content.lower().startswith("!monty help"):
        await display_help(message)
        return

    if message.content.lower().startswith("!monty network"):
        await message.channel.send("Check your direct messages")
        await get_user_data(message)
        return

    if isinstance(message.channel, DMChannel):
        await get_user_data(message)
        return

    if message.content.lower().startswith("!monty connect"):
        await make_connections(message, message.author)


client.run(DISCORD_TOKEN)
