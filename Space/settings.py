import pygame, sys
from random import randint

pygame.init()

WIDTH = 600
HEIGHT = 800
FPS = 60
WINDOW_TITLE = 'Space Shooter'

font = pygame.font.Font('font/stormfaze.ttf', 50)
font2 = pygame.font.Font('font/stormfaze.ttf', 20)
pygame.display.set_caption(WINDOW_TITLE)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


