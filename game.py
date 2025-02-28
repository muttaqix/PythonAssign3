import random
from player import Player
class Game:
    def __init__(self):
        self.players = [Player(),Player(),Player()]
        self.guess = None 

    def start(self):
        self.guess = random.randint(1,6)
        print("The number that was guessed is:",self.guess)
    
    def match(self):
        player_index = 1
        for playerObj in self.players:
            roll_number = Player.roll(self)
            print("Player",player_index, "rolled:", roll_number)
            if roll_number == self.guess:
                print("Player",player_index,"guessed correctly and scored a point")
                playerObj.score +=1
            print("Player",player_index,"score is",playerObj.score)
            player_index +=1
     

playerObj = Player()

