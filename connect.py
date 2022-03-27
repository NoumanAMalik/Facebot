from replit import db
from util import str_to_arr
from person import Person

def matches_to_string(matches):
	string = "List of matches:\n"
	for match in matches:
		string += match + "\n"
	return string

async def make_connections(message, person_calling):
	matches = []

	person_1 = Person.str_to_person(db[f"{person_calling}"])
	person_1_interests = str_to_arr(person_1.interests)
	person_1_courses = str_to_arr(person_1.courses)
	
	for person in db.keys():
		similarities = 0

		if str(person) == str(person_calling):
			continue

		person_2 = Person.str_to_person(db[f"{person}"])
		person_2_interests = str_to_arr(person_2.interests)
		person_2_courses = str_to_arr(person_2.courses)
			
		if person_1.year == person_2.year:
			similarities += 1
	
		for interest in person_1_interests:
			if interest in person_2_interests:
				similarities += 1
	
		for course in person_1_courses:
			if course in person_2_courses:
				similarities += 1

		if int(similarities/2) >= person_1.fit:
			matches.append(person_2.user)

	await message.author.send(matches_to_string(matches))
	return
