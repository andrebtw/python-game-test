from constants import *
from game import *
from events import *
from menu import *
from player import *
from utils import *

def player_movement(game: MyGame) -> MyGame:
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        game.player.moveLeft(game.dt)
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        game.player.moveRight(game.dt)
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        game.running = False
    return game

def game_func(game: MyGame) -> MyGame:
    game.setWallpaperColor(WHITE)
    game.player.drawPlayer(game.screen)
    game = player_movement(game)
    game.refreshScreen()
    return game

def loop(game: MyGame) -> None:
    events = MyEvents()
    game.player.init_test(scaleResX(50), scaleResY(50), scaleResY(20), PLAYER_COLOR)

    while game.running:
        events.startEventCheck()
        if events.events["quit"]:
            game.exitGame()

        game = game_func(game)
        # game = menu(game)
        game.dtLoop()

def main() -> None:
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, IS_FULLSCREEN, FPS)
    loop(game)

if __name__ == "__main__":
    main()
