import os
import discord
from help import display_help
from getData import get_data
# from data import test
# import asgiref.sync
from replit import db

print(db.keys())
keys = db.keys()
for e in keys:
    print(db[e])
    # i though u just vomitted on you keyboard lmfao
	# the TOKEN: OTU3MTI0ODY1MTk2OTcwMDI2.Yj6N_g.0MS7ESSH6cOt_JIkyPjBwekHkWw
	# work in a diff branch
DISCORD_TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
	print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.lower().startswith("!monty help"):
		await display_help(message)
		return

	if message.content.lower().startswith("!monty network"):
		# ToDo
		await message.channel.send("check your dms hehe")
		await get_data(message, True)
		return

	if isinstance(message.channel, discord.DMChannel):
		await get_data(message, False)
		return

client.run(DISCORD_TOKEN)
# print("Discord bot token: {}".format(DISCORD_TOKEN))