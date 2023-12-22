#create a function to receive voice input
#use the speech_recognition library
#use the microphone to listen for a command
#convert the audio to text
#return the text
#use the text to play the game
#use the text to end the game
#use the text to repeat the game
import random
import speech_recognition as sr
#use the text to make a decision
def player_choice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please input a decision. Choose between: Rock, Paper, or Scissors.")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said: {}".format(text))
            return text.lower()
        except:
            print("Sorry, I didn't get that.")
            return "error"
#use the text to end the game
def end_game(text):
    if "end" in text:
        return True
    else:
        return False
#use the text to repeat the game
def repeat_game(text):
    if "repeat" in text:
        return True
    else:
        return False
#use the text to make a decision
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
#use the text to make a decision
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
#use the text to end the game
def end_game(text):
    if "end" in text:
        return True
    else:
        return False
#use the text to repeat the game
def repeat_game(text):
    if "repeat" in text:
        return True
    else:
        return False

    
