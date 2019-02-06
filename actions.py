# UTILS AND FUNCTIONALITY
from data import population, clubs
from components import Club, Person

my_name = "Hamad"
my_age = 26
my_bio = "I am amazing computer engineer "
myself = Person(my_name, my_bio, my_age)


def introduction():
	print("Hello, %s. Welcome to our portal." % my_name)
	print("- - - - - - - - - - - - - - - - -")

	options()


def options():
	# your code goes here!
	print("Would you like to:")
	print("1) Create a new club.")
	print("or:")
	print("2) Browse and join clubs.")
	print("or:")
	print("3) View existing clubs.")
	print("or:")
	print("4) Display members of a club.")
	print("or:")
	print("-1) Close application.")
	option = input("> ")

	if option == "1":
		create_club()
	elif option == "2":
		view_clubs()
		join_clubs()
	elif option == "3":
		view_clubs()
	elif option == "4":
		view_club_members()
	elif option == "-1":
		quit()
	else:
		print("Error! Please choose one of the otions :")
		options()


def create_club():
	# your code goes here!
	club_name = input("Pick a name for your awesome new club: ")
	print("What is your club about?")
	club_descreption = input("Describe your club? ")

	n_club = Club(club_name, club_descreption)
	n_club.assign_president(myself)

	print ("Enter the numbers of the people ypu Would like to recruit to your new club (-1 to stop): ")
	print ("- - - - - - - - - - - - - - - - - -")

	for people in population:
		print ("[%d]  %s" % (population.index(people) + 1, people.name))
	player = input("> ")
	while player != "-1":
		if int(player)>=1 and int(player)<len(population):
			n_club.recruit_member(population[int(player) - 1])
			player = input("> ")
	print ("Here's your club:")
	print (n_club.name)
	print (n_club.description)
	print ("Members: ")

	total_all_age = 0
	n_club.print_member_list()
	clubs.append(n_club)
	print ("Ok %s Club is Successfully Created" % n_club.name)
	options()


def view_clubs():
	# your code goes here!
	for club in clubs:
		print ("NAME: %s" % club.name)
		print ("DESCRIPTION: %s" % club.description)
		print ("MEMBERS: %s" % (len(club.members)))
		print ("")


def view_club_members():
	# your code goes here!
	view_clubs()
	print ("")
	name_of_the_club_memebers = input("Enter the name of the club whose members you'd like to see: ")
	club_objuct = None
	for club in clubs:
		if (club.name == name_of_the_club_memebers):
			club_objuct = club
			for player in club_objuct.members:
				print ("- %s (%s years old) - %s" % (player.name, player.age, player.bio))
				print ("")
	options()


def join_clubs():
	# your code goes here!
	view_clubs()
	print ("")
	name_the_club_join = input("Enter the name of the club you'd like to join: ")
	club_objuct = None
	for club in clubs:
		if (club.name == name_the_club_join):
			club_objuct = club
			club_objuct.recruit_member(myself)
			break
	print ("%s just joined %s" % (myself.name, club_objuct.name))
	options()


def application():
	introduction()
	
	# your code goes here!

