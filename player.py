import pygame

class MyPlayer:
    def __init__(self) -> None:
        pass
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

    def drawPlayer(self, screen):
        pygame.draw.rect(screen,self.color, (self.x_pos, self.y_pos, self.size, self.size))
    
    def moveLeft(self, dt):
        self.x_pos += int(-2)
    
    def moveRight(self, dt):
        self.x_pos += int(2)

