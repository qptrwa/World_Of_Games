import random
from currency_converter import CurrencyConverter
from Utils import BAD_RETURN_CODE

class CurrencyRouletteGame:

    def __init__(self, playername, diffeculty):
        self.playerName = playername
        self.diffeculty = diffeculty
        self.secret_number = 0
        self.c = CurrencyConverter()

    def _generate_number(self):
        self.secret_number = random.randint(1,100)

    def _get_money_interval(self):
        t = self.c.convert(self.secret_number, 'USD', 'ILS')
        d = self.diffeculty
        min = t - (5 - d)
        max = t + (5 - d)

        return min,max

    def _get_guess_from_user(self):
        for z in range(3):
            guess =  input("Please guess the right conversun from " + str(self.secret_number) + " USD to ILS  ")
            if guess.isdigit():
                return int(guess)
        print("failed")
        return BAD_RETURN_CODE


    def play(self):
        print ("Hello " + self.playerName + " and welcome to the CurrencyRouletteGame")
        self._generate_number()
        U = self._get_guess_from_user()
        min,max = self._get_money_interval()
        if min < int(U) < max:
            return True
        return False