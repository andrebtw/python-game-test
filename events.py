import pygame
from game import *

class MyEvents:
    def __init__(self) -> None:
        self.events = {"quit": False}

    def startEventCheck(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.events["quit"] = True