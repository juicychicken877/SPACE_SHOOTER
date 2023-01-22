from settings import *


class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self, player_x):
        super().__init__()

        self.image = pygame.image.load('images/default/bullet-red.png').convert_alpha()
        self.rect = self.image.get_rect(center=(player_x, 650))

        self.speed = 8

    def move_bullet(self):
        self.rect.y -= self.speed

    def isOutOfScreen(self):
        # if out of screen kill bullet
        if (self.rect.y <= 0):
            self.kill()
    
    def update(self):
        self.move_bullet()
        self.isOutOfScreen()

        
class SpaceInvaderBullet(pygame.sprite.Sprite):
    def __init__(self, invader_x, invader_y):
        super().__init__()

        self.image = pygame.image.load('images/default/bullet-red.png').convert_alpha()
        self.rect = self.image.get_rect(center=(invader_x, invader_y))

        self.speed = 10

    def move_bullet(self):
        self.rect.y += self.speed

    def isOutOfScreen(self):
        # if out of screen kill bullet
        if (self.rect.y >= 800):
            self.kill()
    
    def update(self):
        self.isOutOfScreen()
        self.move_bullet()
        

