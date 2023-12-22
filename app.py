#create a game that plays rock paper scissors with the user
#user inputs rock paper or scissors
#computer randomly chooses rock paper or scissors
#compare the two choices and decide who wins
#display the results
#ask the user if they want to play again
#repeat if they do
#end the game if they don't

import random
def player_choice():
    x = input("Please input a decision. Choose between: Rock, Paper, or Scissors.\n").lower()
    return x

def computer_choice():
    integer = random.randint(1,3)
    if integer == 1:
        print("Computer chooses Rock!")
        return "rock"
    elif integer == 2:
        print("Computer chooses Paper!")
        return "paper"
    else:
        print("Computer chooses Scissors!")
        return "scissors"

def compare_choices(player_choice, computer_choice):
    if player_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif player_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    elif player_choice == computer_choice:
        print("It's a tie!")
    else:
        print("You lose!")

pc = player_choice()
cc = computer_choice()
compare_choices(pc, cc)


