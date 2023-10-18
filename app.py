# create a rock paper scissors game using python with GitHub Copilot

# import the random module
import random

# create a list of options
options = ["rock", "paper", "scissors"]

# create the score and round played variables
score = 0
rounds_played = 0

# create the loop to play the game

while True:

    # choose a random option of the list
    computer_choice = random.choice(options)

    # asking for the user input
    player_choice = input("Rock, paper or scissors?  ")

    # if player chose rock 
    if player_choice.lower() == "rock":
        if computer_choice == "rock":
            print("Computer chose rock. It's a tie!")
        elif computer_choice == "paper":
            print("Computer chose paper. You lose!")
        elif computer_choice == "scissors":
            print("Computer chose scissors. You win!")
            score += 1
        rounds_played += 1

    # if player chose paper
    elif player_choice.lower() == "paper":
        if computer_choice == "rock":
            print("Computer chose rock. You win!")
            score += 1
        elif computer_choice == "paper":
            print("Computer chose paper. It's a tie!")
        elif computer_choice == "scissors":
            print("Computer chose scissors. You lose!")
        rounds_played += 1

    # if player chose scissors
    elif player_choice.lower() == "scissors":
        if computer_choice == "rock":
            print("Computer chose rock. You lose!")
        elif computer_choice == "paper":
            print("Computer chose paper. You win!")
            score += 1
        elif computer_choice == "scissors":
            print("Computer chose scissors. It's a tie!")
        rounds_played += 1

    # if player chose something else
    else:
        print("That's not a valid play. Check your spelling!")

    # ask the user if they want to play again and break the loop if they don't
    # if they break the loop, print the score
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() != "y":
        print(f"You played {rounds_played} rounds and got {score} points!")
        break