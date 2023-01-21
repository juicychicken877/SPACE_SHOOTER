from settings import *
from declarations import player_image, shoot
from bullets import Bullet


class Player:
    def __init__(self):
        self.image = player_image
        self.rect = self.image.get_rect(midbottom=(300, 700))

        self.speed = 5

        self.shoot_cooldown = 150

        self.bullet_list = pygame.sprite.Group()

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # going to -x
            if self.rect.left != 0:
                self.rect.x = self.rect.x - self.speed
            else:
                pass

        if keys[pygame.K_d]:
            # going to +x
            if self.rect.right != 600: 
                self.rect.x = self.rect.x + self.speed
            else:
                pass

        if keys[pygame.K_SPACE] and self.shoot_cooldown==0:
            self.shoot()

        else:
            pass

    def shoot(self):
        shoot.play()

        self.bullet_list.add(Bullet(self.rect.centerx))

        self.shoot_cooldown = 150

    def update(self):
        # decreasing the cooldown every frame
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 10
        # bullet list
        self.bullet_list.draw(screen)
        self.bullet_list.update()

        self.input()
        screen.blit(self.image, self.rect) # draw player on the screen