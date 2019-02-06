# CLASSES AND METHODS
class Person():
	def __init__(self, name, bio, age):
		# your code goes here!
		self.name = name
		self.bio = bio
		self.age = age

		

class Club():
	def __init__(self, name, description):
		# your code goes here!
		self.name = name
		self.description = description
		self.president = None
		self.members=[]

	def assign_president(self, person):
		# your code goes here!
		self.president = person

	def recruit_member(self, person):
		# your code goes here!
		self.members.append(person)

	def print_member_list(self):
		# your code goes here!
		total=0.0
		for member in self.members:
			total+= member.age
			if member.name== self.president.name:
				print ("- %s (%s years old, President) - %s" % (member.name, member.age, member.bio))
			else:
				print ("- %s (%s years old) - %s" % (member.name, member.age, member.bio))
		total=total/len(self.members)
		print("Average age: %s yrs" % total)
