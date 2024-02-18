import pygame
from game import *

class MyEvents:
    def __init__(self) -> None:
        pass

    def startEventCheck(self) -> None:
        self.events = {"quit": False}
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.events["quit"] = True