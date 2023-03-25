import random

# create a list of options
options = ["rock", "paper", "scissors"]

# ask user for their choice
user_choice = input("Choose rock, paper, or scissors: ")

# generate a random choice for the computer
computer_choice = random.choice(options)

# print out the user's choice and the computer's choice
print("You chose:", user_choice)
print("The computer chose:", computer_choice)

# determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win!")
else:
    print("The computer wins!")
