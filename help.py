async def display_help(message):
	helpString = """ Hi! I am monty, a bot whose goal is to connect you with people with similar interests.

Type the command 
`!monty network`
and I will dm you a couple questions to set up your profile.

I will then find people who have similar interests, and give both parties each other's discord username so you can contact each other.
		"""
	await message.channel.send(helpString)