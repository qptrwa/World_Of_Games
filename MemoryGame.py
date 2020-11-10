import random
import time
from Utils import screen_clear, BAD_RETURN_CODE

class MemoryGame:

    def __init__(self, playername, diffeculty):
        self.playerName = playername
        self.diffeculty = diffeculty
        self.secret_sequence = []

    def _generate_sequence(self):
        for z in range(self.diffeculty):
            self.secret_sequence.append(str(random.randint(1, 101)))

    def _get_list_from_user(self):
        user_input = []
        for z in range(self.diffeculty):
            guess = input("Write guess #"+str(z)+":  ")
            user_input.append(guess)
        return user_input

    def _is_list_equal(self, game_list, user_list):

        if game_list == user_list:
            return True
        else:
            return False

    def play(self):
        print("Hello " + self.playerName + " and welcome to the MemoryGame")
        self._generate_sequence()
        print(self.secret_sequence)
        time.sleep(0.7)
        screen_clear()
        user_list = self._get_list_from_user()
        res = self._is_list_equal(self.secret_sequence,user_list)
        return res