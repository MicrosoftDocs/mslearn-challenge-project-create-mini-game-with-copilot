import random
print("hello world")

def get_player_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def play_round(player_choice, computer_choice):
    print(f"Player chooses: {player_choice}")
    print(f"Computer chooses: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
        return 'tie'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        print("Player wins!")
        return 'win'
    else:
        print("Computer wins!")
        return 'loss'

def play_game():
    player_score = 0
    computer_score = 0

    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        result = play_round(player_choice, computer_choice)

        if result == 'win':
            player_score += 1
        elif result == 'loss':
            computer_score += 1

        print(f"Player score: {player_score}")
        print(f"Computer score: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Game over!")
    print(f"Final score: Player {player_score} - Computer {computer_score}")

play_game()
