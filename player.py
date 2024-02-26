import pygame

class MyPlayer:
    def __init__(self) -> None:
        self.left = False
        self.right = False
        self.up = False
        self.gravity = 0
        self.gravity_speed = 1
        self.is_falling = False

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

    def upPressed(self, dt) -> None:
        if self.up is not True:
            self.up = True
            self.playerJump(dt)

    def upReleased(self, dt) -> None:
        self.up = False

    def playerJump(self, dt) -> None:
        self.gravity = 50
        self.is_falling = True
        self.y_pos -= 30
        self.gravity += self.gravity_speed
        self.y_pos += int(self.gravity * dt)

    def playerFall(self, dt) -> None:
        if self.y_pos < 700:
            self.gravity += self.gravity_speed
            self.y_pos += int(self.gravity * dt)
        else:
            self.is_falling = False

    def moveLeft(self, dt) -> None:
        self.x_pos += int(-200 * dt)
    
    def moveRight(self, dt) -> None:
        self.x_pos += int(200 * dt)
