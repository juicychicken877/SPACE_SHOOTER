from settings import *
from bars import *


class MainMenu:
    def __init__(self):
        self.background = pygame.image.load('images/backgrounds/main-menu-background-1.jpg').convert_alpha()
        self.start_bar = MainMenuStartGameBar()
        self.logo = MainMenuAnimatedLogo()
        self.exit_bar = MainMenuExitBar()

    def update(self):
        screen.blit(self.background, (0, 0))
        self.logo.update()
        self.exit_bar.update()
        
        return self.start_bar.update()


