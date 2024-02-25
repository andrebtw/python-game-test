from constants import *
from game import *
from events import *
from menu import *
from player import *
from utils import *

def player_movement(game: MyGame) -> MyGame:
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        game.player.leftPressed(game.dt)
    else:
        game.player.leftReleased(game.dt)
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        game.player.rightPressed(game.dt)
    else:
        game.player.rightReleased(game.dt)
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        game.running = False
    return game

def game_func(game: MyGame) -> MyGame:
    game.setWallpaperColor(WHITE)
    game.player.drawPlayer(game.screen)
    game = player_movement(game)
    game.refreshScreen()
    print(game.dt)
    return game

def loop(game: MyGame) -> None:
    events = MyEvents()
    game.player.init_test(scaleResX(700), scaleResY(720 - 20), scaleResY(20), PLAYER_COLOR)

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
