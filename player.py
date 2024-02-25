import pygame

class MyPlayer:
    def __init__(self) -> None:
        self.left = False
        self.right = False
    def init(self, x_pos: int, y_pos: int, size: int, image: str) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.size = size
        self.image = image
    
    def init_test(self, x_pos: int, y_pos: int, size: int, color: tuple) -> None:
        self.size = size
        self.color = color
        self.x_pos = x_pos
        self.y_pos = y_pos

    def drawPlayer(self, screen) -> None:
        pygame.draw.rect(screen,self.color, (self.x_pos, self.y_pos, self.size, self.size))
    
    def leftPressed(self, dt) -> None:
        if self.right is not True:
            self.left = True
            self.moveLeft(dt)

    def rightPressed(self, dt) -> None:
        if self.left is not True:
            self.right = True
            self.moveRight(dt)

    def leftReleased(self, dt) -> None:
        self.left = False

    def rightReleased(self, dt) -> None:
        self.right = False

    def moveLeft(self, dt) -> None:
        self.x_pos += int(-2)
    
    def moveRight(self, dt) -> None:
        self.x_pos += int(2)

