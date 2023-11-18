import random

def get_player_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower().strip()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid choice. Please choose again.")

def generate_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "lose"

def play_game():
    """
    This function allows the player to play a game against the computer.
    It keeps track of the number of rounds played, player wins, and computer wins.
    At the end, it determines the overall winner based on the number of wins.
    """

    # Initialize variables
    player_wins = 0
    computer_wins = 0
    rounds = 0

    while True:
        rounds += 1

        # Get player's choice
        player_choice = get_player_choice()

        # Generate computer's choice
        computer_choice = generate_computer_choice()

        # Print player and computer choices
        print(f"Player chooses: {player_choice}")
        print(f"Computer chooses: {computer_choice}")

        # Determine the winner of the round
        result = determine_winner(player_choice, computer_choice)

        if result == "win":
            print("You win!")
            player_wins += 1
        elif result == "lose":
            print("You lose!")
            computer_wins += 1
        else:
            print("It's a tie!")

        # Print current score
        print(f"Player wins: {player_wins}")
        print(f"Computer wins: {computer_wins}")

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower().strip()

        # Validate the input
        while play_again not in ["yes", "no", "y", "n"]:
            print("Invalid choice. Please choose again.")
            play_again = input("Do you want to play again? (yes/no): ").lower().strip()

        if play_again in ["no", "n"]:
            break

    # Print final results
    print(f"Total rounds played: {rounds}")
    print(f"Player wins: {player_wins}")
    print(f"Computer wins: {computer_wins}")

    # Determine the overall winner
    if player_wins > computer_wins:
        print("You are the overall winner!")
    elif player_wins < computer_wins:
        print("Computer is the overall winner!")
    else:
        print("It's a tie!")

play_game()
