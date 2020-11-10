import random
from Utils import BAD_RETURN_CODE

class Guessgame:

    def __init__(self, playername, diffeculty):
        self.playerName = playername
        self.diffeculty = diffeculty
        self.secret_number = -1

    def _generate_number(self):
        self.secret_number = random.randint(1, self.diffeculty)

    def _get_guess_from_user(self):

        for z in range(3):
            guess =  input("Please write your guess between 1 to " + str(self.diffeculty) + "  ")
            # check its a number between 1 and dif

            if guess.isdigit() and 1 <= int(guess) <= self.diffeculty:
                # if valid - return number
                return guess

        #else guess again - 3 tries
        print("failed")
        return BAD_RETURN_CODE

    def _compare_results(self):
        number = self._get_guess_from_user()
        if number  != BAD_RETURN_CODE:
            # compare results
            if number == str(self.secret_number):
                return True
        return False

    def play_the_game(self):
        print ("Hello " + self.playerName + " and welcom to the Guessgame")
        self._generate_number()
        res =  self._compare_results()
        print(self.secret_number)
        return res