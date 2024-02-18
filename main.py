from game import *
from events import *
from menu import *

def loop(game: MyGame) -> None:
    while game.running:
        game.startEventCheck()
        if game.events["quit"]:
            game.exitGame()

        game = menu(game)
        game.dtLoop()

def main() -> None:
    width = 1280
    height = 720
    isFullscreen = False
    fps = 60
    game = MyGame(width, height, isFullscreen, fps)
    loop(game)

if __name__ == "__main__":
    main()