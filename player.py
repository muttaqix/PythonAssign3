import random
class Player:
    def __init__(self):
        self.score = 0

    def roll(self):
        return random.randint(1,6)


