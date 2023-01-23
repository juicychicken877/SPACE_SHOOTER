from settings import *
from bullets import SpaceInvaderBullet


class SpaceInvader(pygame.sprite.Sprite):
    def __init__(self, x, type):
        super().__init__()
        self.image_blue = pygame.image.load('images/default/space-invader.png').convert_alpha()
        self.image_green = pygame.image.load('images/default/space-invader-green.jpg').convert_alpha()
        self.image_purple = pygame.image.load('images/default/space-invader-purple.png').convert_alpha()
        
        if type == 'blue':
            self.image = self.image_blue
        elif type == 'green':
            self.image = self.image_green
        else:
            self.image = self.image_purple

        self.rect = self.image.get_rect(center=(x, -100))

        self.HP = 100
        self.speed = 3
        self.shot_cooldown = 3000

        self.shot_sound = pygame.mixer.Sound('sounds/shoot.wav')
        self.shot_sound.set_volume(0.1)

        self.bullets_list = pygame.sprite.Group()

    def move(self):
        self.rect.y += self.speed

    def isCollidingWithBullet(self, bullet_list):
        # kill a bullet if colliding with enemy
        if pygame.sprite.spritecollide(self, bullet_list, True):
            self.kill()

    def attack(self):
        if self.shot_cooldown <= 0:
            self.bullets_list.add(SpaceInvaderBullet(self.rect.centerx, self.rect.centery))
            self.shot_cooldown = randint(3000, 3500)
            self.shot_sound.play()

    def isAlive(self):
        if self.rect.y > 900:
            self.kill()
        else:
            pass

    def update(self, bullet_list):
        if self.shot_cooldown > 0:
            self.shot_cooldown -= 20
        self.bullets_list.draw(screen)
        self.bullets_list.update()
        self.attack()
        self.move()
        self.isAlive()
        self.isCollidingWithBullet(bullet_list)
