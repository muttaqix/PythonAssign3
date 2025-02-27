import random
class Game:
    def __init__(self,players,guess):
        self.players = ["player1","player2","player3"]
        self.guess = None 

    def start(self):
        self.guess = random.randint(1,6)
    
    def match(self):
        
