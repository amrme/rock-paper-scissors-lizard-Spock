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


# the main function
def rpsls(player_choice):
	# user's choice and processing 
	print ""
	print "You can choose one of the following: rock, Spock, paper, lizard, scissors."
	player_number = name_to_number(player_choice)

	# computer's choice and processing
	comp_number = random.randrange(0, 4, 1)
	comp_choice = number_to_name(comp_number)
	print "Computer chose", comp_choice

	# logic
	result = (comp_number - player_number) % 5
	if (result == 1 or result == 2):
        print "Computer is the winner!"
    elif (result == 3 or result == 4):
        print "You win!"
    else:
        print "You both tie!"


# test 
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")















