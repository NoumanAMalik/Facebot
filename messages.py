async def display_help(message):
    string = """
>>> Hi! I'm Monty the Python bot, my goal is to connect you with other people that have similar interests.
    
Here are a list of commands to get you on your way:
`!monty network`
 I will ask you some questions to set up your profile.
	
`!monty connect`
 I will give you a list of matches, who you can then message.
    
Here are a list of some other utility and *fun* commands
`!monty python`
`!monty help`
"""

    await message.channel.send(string)

# This is an easter egg and a play on words. Python the language was named after Monty Python the comedy.
# This bot is named Monty since it is built from python. When a user execute the command monty python, the ode
# ode of python is returned to them.
	
async def ode_of_monty(message):
    string = """
>>> Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one- and preferably only one -obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
    await message.channel.send(string)