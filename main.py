from game import Game

if __name__ == "__main__":
    while True:
        game = Game()
        result = game.run()
        if result == "Quit":
            break
