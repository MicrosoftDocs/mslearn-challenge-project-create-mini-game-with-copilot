# write 'hello world' to the console
#print('hello world')

# create a rock paper scissors game
# The rock, paper, scissors game is a hand game in which each player chooses one of the three tools and these will be compared to see who wins.
# The winner of the game is based in three simple rules: #
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.
# If both players choose the same tool, the game ends in a tie.
# The game will be implemented in the following way:
# The computer will randomly choose one of the three tools.
# The user will enter their name.
# The user will choose one of the three tools.
# A message indicating who won the game will be displayed.
# The game will be implemented using the following steps:
# Import the random module.
# Define a list of the three tools: rock, paper, and scissors.
# Define a variable that will store the name of the user.
# Define a variable that will store the name of the computer.
# Define a variable that will store the tool chosen by the user.
# Define a variable that will store the tool chosen by the computer.
# Define a variable that will store the result of the game.
# Define a function that will print the message indicating who won the game.
# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
#At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
#By the end of each round, the player can choose whether to play again.
#Display the player's score at the end of the game.
#The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.

import random
tools = ['rock', 'paper', 'scissors']
user_name = input('Enter your name: ')
computer_name = 'Computer'
user_tool = ''
computer_tool = ''
result = ''
user_score = 0
computer_score = 0
def print_result(result):
    if result == 'win':
        print('You won!')
    elif result == 'lost':
        print('You lost!')
    elif result == 'tie':
        print('It\'s a tie!')
    else:
        print('Invalid option!')
while True:
    user_tool = input('Choose your tool (rock, paper, scissors): ').lower()
    if user_tool not in tools:
        print_result('invalid')
        continue
    computer_tool = random.choice(tools)
    print(f'{user_name} chose {user_tool}')
    print(f'{computer_name} chose {computer_tool}')
    if user_tool == computer_tool:
        print_result('tie')
    elif user_tool == 'rock' and computer_tool == 'scissors':
        print_result('win')
        user_score += 1
    elif user_tool == 'scissors' and computer_tool == 'paper':
        print_result('win')
        user_score += 1
    elif user_tool == 'paper' and computer_tool == 'rock':
        print_result('win')
        user_score += 1
    else:
        print_result('lost')
        computer_score += 1
    print(f'{user_name} score: {user_score}')
    print(f'{computer_name} score: {computer_score}')
    play_again = input('Play again? (y/n): ').lower()
    if play_again != 'y':
        break
print(f'{user_name} final score: {user_score}')
print(f'{computer_name} final score: {computer_score}')
if user_score > computer_score:
    print(f'{user_name} won the game!')
elif user_score < computer_score:
    print(f'{computer_name} won the game!')
else:
    print('The game ended in a tie!')
    