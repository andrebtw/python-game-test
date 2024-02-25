import pygame
from constants import *

def scaleResX(px: int):
    return ((px * SCREEN_WIDTH) / 1280)

def scaleResY(px: int):
    return ((px * SCREEN_HEIGHT) / 720)
