#create a pythoon multiplayer mini game where the computer will be your opponent and can randomly choose one of the elements (rock, paper, or scissors) for each move, just like you. Your interaction in the game will be through the console (Terminal).
#The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
#At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
#By the end of each round, the player can choose whether to play again.
#Display the player's score at the end of the game.
#the gamme should continue until the player decides to quit.
#The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.

print("Welcome to the Rock, Paper, Scissors game!")
print("You will be playing against the computer.")
print("You will be asked to choose between Rock, Paper, or Scissors.")
print("The computer will randomly choose one of the three options.")
print("The game will then determine who won the round.")
print("The game will continue until you decide to quit.")
print(" ")
print("Good luck!")
print(" ")
print(" ")
print(" ")

import random
import sys

#defining the variables
player_score = 0
computer_score = 0
ties = 0
rounds = 0
player_choice = ""
computer_choice = ""
options = ["rock", "paper", "scissors"]

#defining the functions
def player_input():
    global player_choice
    player_choice = input("Please choose between rock, paper, or scissors: ")
    player_choice = player_choice.lower()
    if player_choice not in options:
        print("Invalid input. Please try again.")
        player_input()
    else:   
        print("You chose " + player_choice + ".")
        print(" ")
        print(" ")

def computer_input():
    global computer_choice
    computer_choice = random.choice(options)
    print("The computer chose " + computer_choice + ".")
    print(" ")
    print(" ")

def determine_winner():
    global player_score
    global computer_score
    global ties
    global rounds
    if player_choice == computer_choice:
        print("It's a tie!")
        ties += 1
    elif player_choice == "rock" and computer_choice == "paper":
        print("The computer wins this round!")
        computer_score += 1
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You win this round!")
        player_score += 1
    elif player_choice == "paper" and computer_choice == "rock":
        print("You win this round!")
        player_score += 1
    elif player_choice == "paper" and computer_choice == "scissors":
        print("The computer wins this round!")
        computer_score += 1
    elif player_choice == "scissors" and computer_choice == "rock":
        print("The computer wins this round!")
        computer_score += 1
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win this round!")
        player_score += 1
    print(" ")
    print(" ")
    rounds += 1

def play_again():
    global player_score
    global computer_score
    global ties
    global rounds
    player_score = 0
    computer_score = 0
    ties = 0
    rounds = 0
    play_again = input("Would you like to play again? (y/n): ")
    if play_again == "y":
        print(" ")
        print(" ")
        print(" ")
        print(" ")  
        game()
    elif play_again == "n":
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("Thanks for playing!")
        #print the score and then exit the game
        print("Your score: " + str(player_score))
        print("Computer score: " + str(computer_score))
        print("Ties: " + str(ties))
        print("Rounds played: " + str(rounds))
        sys.exit()
    else:
        print("Invalid input. Please try again.")
        play_again()

def game():
    while True:
        player_input()
        computer_input()
        determine_winner()
        print("Your score: " + str(player_score))
        print("Computer score: " + str(computer_score))
        print("Ties: " + str(ties))
        print("Rounds played: " + str(rounds))
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        play_again()
game()