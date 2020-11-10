from GuessGame import Guessgame
from MemoryGame import MemoryGame
from CurrencyRouletteGame import CurrencyRouletteGame
from Score import add_score
class UserName:

    def __init__(self, name):
        self.name = name

    def welcome(self):
        print("Hello " + self.name + " and welcome to the World of Games (WoG)")
        print('Here you can find many cool games to play.')

    def getName(self):
        return self.name

class ChooseGame:

    def __init__(self,playerName, game, diffeculty):
        self.playerName = playerName
        self.game = game
        self.diffeculty = diffeculty

    def _win_or_lose(self,res):
        if res:
            print("WIN")
            add_score(int(self.diffeculty))
        else:
            print("LOSER!")

    def games(self):
        if self.game == '1':
            print("You Chose Memory Game difficulty level : " + self.diffeculty)
            myGame = MemoryGame(self.playerName, int(self.diffeculty))
            self._win_or_lose(myGame.play())
        elif self.game == '2':
            print("You Chose Guess Game difficulty level : " + self.diffeculty)
            myGame = Guessgame(self.playerName,int(self.diffeculty))
            self._win_or_lose(myGame.play_the_game())
        elif self.game == '3':
            print("You Chose Currency Roulette difficulty level : " + self.diffeculty)
            myGame = CurrencyRouletteGame(self.playerName,int(self.diffeculty))
            self._win_or_lose(myGame.play())