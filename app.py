import random

class Game:
    def __init__(self):
        self.user_win = 0
        self.computer_win = 0

    def play(self):
        user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
        if user not in ['r', 'p', 's']:
            print('Invalid input')
            self.play()
        computer = random.choice(['r', 'p', 's'])

        if user == computer:
            print('It\'s a tie')
        else:
            if self.is_win(user, computer):
                self.user_win += 1
                print('You won!')
            else:
                self.computer_win += 1
                print('You lost!')

        self.again()

    def again(self):
        play_again = input("\nDo you want to play again? (y/n)\n If you want to see the score type 'screen'\n")
        if play_again.lower() == "y":
            self.play()
        else:
            if play_again.lower() == "screen":
                print("Wins: " + str(self.user_win))
                print("Looses: " + str(self.computer_win))
                self.again()
            else:
                print("Thanks for playing!")
                return

    def is_win(self, player, opponent):
        if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
                or (player == 'p' and opponent == 'r'):
            return True

game = Game()
game.play()