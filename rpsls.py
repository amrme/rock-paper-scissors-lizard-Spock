# Rock-paper-scissors-lizard-Spock Game

''' name could be:
				0 — rock
				1 — Spock
				2 — paper
				3 — lizard
				4 — scissors
'''

# name_to_number function takes in a name and returns it's corresponding number
def name_to_number(name):
	if (name == "rock"):
		return 0
	elif (name == "Spock"):
		return 1
	elif (name == "paper"):
		return 2
	elif (name == "lizard"):
		return 3
	elif (name == "scissors"):
		return 4
	else:
		print "That name is invalid"
	return -1

# number_to_name function takes in a number and returns back it's corresponding name
def number_to_name(number):
	if (number == 0):
		return "rock"
	elif (number == 1):
		return "Spock"
	elif (number == 2):
		return "paper"
	elif (number == 3):
		return "lizard"
	elif (number == 4):
		return "scissors"
	else:
		print "Invalid numebr"
	return -2

