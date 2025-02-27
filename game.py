import random
from player import Player
class Game:
    def __init__(self,players,guess):
        self.players = ["player1","player2","player3"]
        self.guess = None 

    def start(self):
        self.guess = random.randint(1,6)
    
    def match(self):
        for i in self.players:
            if self.roll == self.guess:
                self.score +=1
                

