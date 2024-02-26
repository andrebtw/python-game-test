from constants import *
from game import *
from events import *
from menu import *
from player import *
from utils import *

def player_movement(game: MyGame) -> MyGame:
    # Controls

    # Left
    if pygame.key.get_pressed()[pygame.K_a]:
        game.player.leftPressed(game.dt)
    else:
        game.player.leftReleased(game.dt)

    # Right
    if pygame.key.get_pressed()[pygame.K_d]:
        game.player.rightPressed(game.dt)
    else:
        game.player.rightReleased(game.dt)

    # Jump
    if pygame.key.get_pressed()[pygame.K_w]:
        game.player.upPressed(game.dt)
    else:
        game.player.upReleased(game.dt)

    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        game.running = False
    
    # Gravity
    game.player.playerFall(game.dt)
    return game

def game_func(game: MyGame) -> MyGame:
    game.setWallpaperColor(WHITE)
    game.player.drawPlayer(game.screen)
    game = player_movement(game)
    game.refreshScreen()
    # print(game.dt)
    return game

def loop(game: MyGame) -> None:
    events = MyEvents()
    game.player.init_test(scaleResX(700), scaleResY(720 - 20), scaleResY(20), PLAYER_COLOR)

    while game.running:
        events.startEventCheck()
        if events.events["quit"]:
            game.exitGame()

        game = game_func(game)
        # print(game.clock.get_fps())
        # game = menu(game)
        game.dtLoop()

def main() -> None:
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, IS_FULLSCREEN, FPS)
    loop(game)

if __name__ == "__main__":
    main()
