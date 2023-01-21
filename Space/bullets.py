from settings import *
from declarations import bullet

class Bullet(pygame.sprite.Sprite):
    def __init__(self, player_x):
        super().__init__()

        self.image = bullet
        self.rect = self.image.get_rect(center=(player_x, 650))

        self.speed = 8

    def move_bullet(self):
        self.rect.y -= self.speed

    def isOutOfScreen(self):
        # if out of screen kill bullet
        if (self.rect.y <= 0):
            self.kill()

    def update(self):
        self.isOutOfScreen()
        self.move_bullet()
