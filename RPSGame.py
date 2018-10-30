from random import randint

choices = ["Rock", "Paper", "Scissors"]

computer_choice = choices[randint(0,2)]
c_lives = 3
p_lives = 3


print("computer chooses: ", computer_choice)

player = False

while player == False:

    print("Your lives:", p_lives)
    print("Computer lives:", c_lives)
    print("choose your weapon")
    player = input("Rock, Paper or Scissors ?\n")

if player == "quit":
	exit()

	print("Player chooses:", player)
	print("Computer chooses:", computer_choice)

	if player == "restart":
		c_lives = 3
		p_lives = 3
		
	player = False

	computer_choice = choices[randint(0,2)]


if player == computer_choice: #tie
	print("Tie")

elif player == "Rock":
	if computer_choice == "Paper":
		c_lives = c_lives - 1
		print("loss")
	else:
		p_lives = p_lives - 1
		print("win", player, "smashes", computer_choice)

elif player == "Paper":
	if computer_choice == "Scissors":
		c_lives = c_lives - 1
		print("loss")
	else:
		p_lives = p_lives - 1
		print("win", player, "covers", computer_choice)

elif player == "Scissors":
	if computer_choice == "Rock":
		c_lives = c_lives - 1
		print("loss")
	else:
		p_lives = p_lives - 1
		print("win", player, "cuts", computer_choice)

else:
	print("check your spelling... thats not a valid choice\n")

if player == "quit":
	print("Rock, Paper, or Scissors")

# reset game loop
	player = False
	computer_choice = choices[randint(0,2)]
