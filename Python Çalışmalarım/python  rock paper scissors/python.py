import random

rockpaperscissors = ["rock", "paper", "scissors"]

def play(player_choice):
    computer_choice = random.choice(rockpaperscissors)
    if computer_choice == "rock":
        if player_choice == "rock":
            return "Nobody wins", computer_choice
        elif player_choice == "paper":
            return "You win", computer_choice
        else:
            return "Computer wins", computer_choice
    elif computer_choice == "paper":
        if player_choice == "rock":
            return "Computer wins", computer_choice
        elif player_choice == "paper":
            return "Nobody wins", computer_choice
        else:
            return "You win", computer_choice
    else: # computer_choice == "scissors"
        if player_choice == "rock":
            return "You win", computer_choice
        elif player_choice == "paper":
            return "Computer wins", computer_choice
        else:
            return "Nobody wins", computer_choice

player_choice = input("Choose rock, paper, or scissors: ")
result, computer_choice = play(player_choice)
print(f"Computer chose {computer_choice}, {result}")
