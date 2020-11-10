from Live import UserName, ChooseGame
import sys

sigh_in = UserName(input("Please enter your name:  "))
sigh_in.welcome()

def _input_choosen_game():
    return input("Please choose a game to play:\n"
        + "1. Memory Game - a sequence of numbers will appear for 1 second and you have toguess it back\n"
        + "2. Guess Game - guess a number and see if you chose like the computer\n"
        + "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"
        + "Please write you choose here: ")

def _validate_chosen_game(x):
    if x == "1" or x =="2" or x == "3":
        return True
    return False

flagValidInput = False
for z in range(3):
    game = _input_choosen_game()
    if  _validate_chosen_game(game):
        flagValidInput = True
        break

if not flagValidInput:
    print("Too many tries to input the game number!!! GoodBye")
    sys.exit(1)

def _input_diffeculty_level():
    return input("Please choose diffeculty between 1 - 5: ")

def _validate_diffeculty_level(y):
    if y == "1" or y == "2" or y == "3" or y == "4" or y == "5":
        return True
    return False

flagValidInput = False
for z in range(3):
    diffeculty = _input_diffeculty_level()
    if _validate_diffeculty_level(diffeculty):
        flagValidInput = True
        break

if not flagValidInput:
    print("Too many tries to input diffeculty!!!")
    sys.exit(1)

choose = ChooseGame(sigh_in.getName(),game,diffeculty)

choose.games()