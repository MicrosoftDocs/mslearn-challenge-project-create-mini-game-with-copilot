# Player chooses rock, paper, or scissors
# Check if the player's choice is valid and inform if not
# Randomly choose an option for the computer
# Determine the winner of the round based on choices
# Display the result and update the player's score
# Ask if the player wants to play again
# End the game and display the final score

import random

valid_choices = ["rock", "paper", "scissors"]
player_score = 0

def play_game():
    global player_score
    player_choice = input("Choose rock, paper, or scissors: ")

    if player_choice not in valid_choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == "yes":
            play_game()
        else:
            print(f"Game over. Final score: {player_score}")
    else:
        computer_choice = random.choice(valid_choices)

        if player_choice == computer_choice:
            result = "It's a tie!"
        elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
            result = "You win!"
            player_score += 1
        else:
            result = "Computer wins!"

        print(f"Player chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        print(result)

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == "yes":
            play_game()
        else:
            print(f"Game over. Final score: {player_score}")

play_game()

