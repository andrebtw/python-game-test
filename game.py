import pygame

class MyGame:
    def __init__(self, width: int, height: int, isFullscreen: bool, fps: int) -> None:
        pygame.init()
        if (isFullscreen):
            self.screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN, vsync=0)
        else:
            self.screen = pygame.display.set_mode((width, height))
        self.dt = 0
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = fps
        print("Game started.")

    def setNewRes(self, width: int, height: int, isFullscreen: bool, isResizable: bool, vsync_nb: int):
        if (isFullscreen):
            self.screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN, vsync=vsync_nb)
        else:
            if (isResizable):
                self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            else:
                self.screen = pygame.display.set_mode((width, height))

    def refreshScreen(self) -> None:
        pygame.display.flip()

    def exitGame(self) -> None:
        self.running = False
        print("Game exited.")

    def dtLoop(self) -> None:
        self.dt = self.clock.tick(self.fps) / 1000

    def keyCheck(self) -> None:
        pass