from game import Game
class Application:
    def __init__(self):
        self.game = Game()
    def run(self):
        for rounds in range(1,6):
            self.game.start()
            self.game.match()


if __name__ == "__main__":
    app = Application()
    app.run()
        
