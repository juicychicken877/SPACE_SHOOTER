from settings import *
from declarations import *


class MainMenu:
    def __init__(self):
        self.background = background_black1

    def draw(self):
        screen.blit(self.background, (0, 0))

