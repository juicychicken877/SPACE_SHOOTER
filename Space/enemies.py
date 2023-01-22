from settings import *
from bullets import SpaceInvaderBullet


class SpaceInvader(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = pygame.image.load('images/default/space-invader.png').convert_alpha()
        self.rect = self.image.get_rect(center=(x, -100))

        self.HP = 100
        self.speed = 2
        self.shot_cooldown = 2000
        self.count = 0
        self.shot_sound = pygame.mixer.Sound('sounds/shoot.wav')
        self.shot_sound.set_volume(0.1)
        self.bullets_list = pygame.sprite.Group()

    def move(self):
        self.rect.y += self.speed

    def isCollidingWithBullet(self, bullet_list):
        # kill a bullet if colliding with enemy
        if pygame.sprite.spritecollide(self, bullet_list, True):
            self.HP -= randint(10, 40)

    def attack(self):
        if self.shot_cooldown <= 0:
            self.bullets_list.add(SpaceInvaderBullet(self.rect.centerx, self.rect.centery))
            self.shot_cooldown = randint(1500, 2500)
            self.shot_sound.play()

    def drawHPBar(self):
        pygame.draw.rect(screen, 'Red', pygame.Rect(self.rect.x, self.rect.y-20, self.HP, 10))

    def isAlive(self):
        if self.rect.y > 900:
            print('space invader killed by black hole')
            print('======')
            self.kill()
        if self.HP > 0:
            pass
        else:
            self.kill()

    def update(self, bullet_list):
        if self.shot_cooldown > 0:
            self.shot_cooldown -= 20
        self.bullets_list.draw(screen)
        self.bullets_list.update()
        self.attack()
        self.drawHPBar()
        self.move()
        self.isAlive()
        self.isCollidingWithBullet(bullet_list)
