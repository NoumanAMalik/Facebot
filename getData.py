from replit import db
# from database import add_person
from person import Person

getYear = False
getCourses = False
getInterests = False
getPref = False

year = None
courses = None
interests = None
pref = None

async def get_data(message, firstMessage):
	global getYear, getCourses, getInterests, getPref, year, courses, interests, pref
	if firstMessage:
		await message.author.send("Hi {0.author}, I will ask a couple of questions to make a profile for you in our database.".format(message))
		await message.author.send("Please enter what year you are currently in (1st year, 2st year, 3st year, 4st year)")
		getYear = True
	else:
		if getYear: 
			year = int(message.content[0])
			getYear = False
			getCourses = True
			await message.author.send("Now please enter the course codes for your current classes")
		elif getCourses:
			courses = message.content
			getCourses = False
			getInterests = True
			await message.author.send("Now please enter your interests")
		elif getInterests:
			interests = message.content
			getInterests = False
			getPref = True
			await message.author.send("Now please enter a number between 1 and 5 for how well of a match you want")
		elif getPref:
			pref = int(message.content)
			getPref = False
			await message.author.send("Thank you for your information")
			print(year)
			print(courses)
			print(interests)
			print(pref)

			cur_per = Person(message.author, year, courses, interests, pref)
			db[cur_per.user] = cur_per.user + " " + str(cur_per.year) + " " + cur_per.courses + " " + cur_per.interests + " " + str(cur_per.fit)
			return
			# This would be when all the data is collected and now we need to create the object and add to the dict and find matches


# can you initialize a person here with the variables i declared up top