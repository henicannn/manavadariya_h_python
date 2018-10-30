# import the random package so that we can generate random numbers
from random import randint

# choices is and array => a container that can hold multiple items
# arrays are 0-based -> the first item is 0, the second is 1, etc
choices = ["Rock", "Paper","Scissors"]

# make the computer choose a weapon from the choices array at random
computer_choice = choices[randint(0,2)]

c_lives = 3
p_lives = 3

# print the choice to the terminal window
print("computer chooses: ", computer_choice)

#set up our loop
player = False

while player == False:
# set player to True by making a selection

	print("choose your weapon")
	player = input("Rock, Paper or Scissors?\n")
	print(player, "\n")

if player == computer_choice: #tie
	print("tie")

elif player == "Rock":
	if computer_choice == "Paper":
		c_lives -=1
		print("loss")
	else:
		p_lives -=1
		print("win", player, "smashes", computer_choice)

elif player == "Paper":
	if computer_choice == "Scissors":
		c_lives -=1
		print("loss")
	else:
		p_lives -=1
		print("win", player, "covers", computer_choice)

elif player == "Scissors":
	if computer_choice == "Rock":
		c_lives -=1
		print("loss")
	else:
		p_lives -=1
		print("win", player, "cuts", computer_choice)

else:
	print("check your spelling... thats not a valid choice\n")

# reset game loop
	player = False
	computer_choice = choices[randint(0,2)]
