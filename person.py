
"""
This class is a blueprint for the objects that will be stored in the database.
"""
class Person:
	def __init__(self, user, year, courses, interests, fit=1):
		self.user = user
		self.year = year
		self.courses = courses
		self.interests = interests
		self.fit = fit
	
	def __str__(self):
		return f"{self.user}|{str(self.year)}|{self.courses}|{self.interests}|{str(self.fit)}"

	@staticmethod
	def str_to_person(person_str):
		person = person_str.split("|")
		return Person(person[0], int(person[1]), person[2], person[3], int(person[4]))

