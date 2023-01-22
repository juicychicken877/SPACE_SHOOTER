from settings import *
from bullets import PlayerBullet


class Player:
    def __init__(self):
        self.image = pygame.image.load('images/xcf/ship-1.xcf').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(300, 680))
        self.speed = 7
        # self.HP = 5
        self.ammo = 100
        self.max_ammo = 100

        self.shoot_cooldown = 100
        self.shots_fired = 0

        self.shoot_sound = pygame.mixer.Sound('sounds/shoot.wav')
        self.shoot_sound.set_volume(0.1)
        # self.no_ammo_warning = font.render('NO AMMO', False, 'Red').convert()
        # self.ammo_warning_rect = self.no_ammo_warning.get_rect(center=(300, 400))

        # self.game_over_warning = font.render('GAME OVER', False, 'Red').convert()
        # self.game_over_rect = self.game_over_warning.get_rect(center=(300,400))
        self.bullet_list = pygame.sprite.Group()

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # going to -x
            if self.rect.left >= 0:
                self.rect.x = self.rect.x - self.speed
            else:
                pass

        if keys[pygame.K_d]:
            # going to +x
            if self.rect.right <= 600: 
                self.rect.x = self.rect.x + self.speed
            else:
                pass

        if keys[pygame.K_SPACE] and self.shoot_cooldown==0:
            self.shoot()

        else:
            pass

    def shoot(self):
        # if self.ammo > 0:
        self.shoot_sound.play()
        # self.ammo -= 1
        self.bullet_list.add(PlayerBullet(self.rect.centerx))
        self.shoot_cooldown = 100
        self.shots_fired += 1

        # elif self.ammo == 0:
            # if dont have ammo
            # screen.blit(self.no_ammo_warning, self.ammo_warning_rect)
    def displayShotsFiredHud(self):
        shots_fired_surf = font2.render('SHOTS FIRED:', False, 'Black').convert()
        shots_fired_count = font2.render(f'{self.shots_fired}', False, 'Black').convert()
        screen.blit(shots_fired_surf, (10, 730))
        screen.blit(shots_fired_count, (200, 730))

    def isShot(self, enemies_group):
        for sprite in enemies_group:
            for bullet in sprite.bullets_list:
                # if bullet collides with a player
                if bullet.rect.bottom >= self.rect.top and bullet.rect.left >= self.rect.left and bullet.rect.right <= self.rect.right:
                    bullet.kill()
                else:
                    pass

    def update(self, enemies_group):
        # decreasing the cooldown every frame
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 10
        # bullet list
        self.bullet_list.draw(screen)
        self.bullet_list.update()
        self.isShot(enemies_group)
        self.input()
        self.displayShotsFiredHud()
        screen.blit(self.image, self.rect) # draw player on the screen
