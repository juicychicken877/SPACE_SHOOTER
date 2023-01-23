from settings import *

menu_bar = pygame.image.load('images/default/main-menu-bar-blue.png').convert_alpha()
exit_bar = pygame.image.load('images/default/game-hud-exit-bar.png').convert_alpha()
game_activated = False
game_exited = False


# bar that you can see below the player when you play
class HudGameLowBar:
    def __init__(self):
        global SCORE
        self.font = pygame.font.Font('font/stormfaze.ttf', 25)
        self.font2 = pygame.font.Font('font/stormfaze.ttf', 40)

        self.exit_bar = exit_bar
        self.exit_bar_rect = self.exit_bar.get_rect(center=(520, 762))
        self.exit_text = self.font2.render('EXIT', False, 'Black')
        self.exit_text_rect = self.exit_text.get_rect(midtop=(520, 742))

        self.ammo_image = pygame.image.load('images/xcf/game-hud-bullet.xcf').convert_alpha()
        self.ammo_rect = self.ammo_image.get_rect(midleft=(10, 762))

    def drawExitBar(self):
        screen.blit(self.exit_bar, self.exit_bar_rect)
        screen.blit(self.exit_text, self.exit_text_rect)

    def drawAmmunition(self, player_ammo, player_max_ammo):
        self.ammo_number = self.font2.render('INF', False, 'Black').convert()
        self.ammo_number_rect = self.ammo_number.get_rect(center=(100, 745))

        self.max_ammo = self.font2.render(f'{player_max_ammo}', False, 'Black').convert()
        self.max_ammo_rect = self.max_ammo.get_rect(center=(100, 780))

        screen.blit(self.ammo_image, self.ammo_rect)
        screen.blit(self.ammo_number, self.ammo_number_rect)
        screen.blit(self.max_ammo, self.max_ammo_rect)

    def isExitBarClicked(self):
        global game_exited, game_activated
        pos = pygame.mouse.get_pos()
        mouse_x = pos[0]
        mouse_y = pos[1]

        if mouse_x >= 470 and mouse_x <= 570 and mouse_y >= 735 and mouse_y <= 790:
            pygame.draw.rect(screen, 'Red', pygame.Rect(465, 730, 110, 65))

            if pygame.mouse.get_pressed()[0]:
                game_exited = True
                game_activated = False

        return game_exited

    def update(self, player_ammo, player_max_ammo):
        pygame.draw.rect(screen, 'Gray',pygame.Rect(0, 725, 600, 75))
        # HP BAR
        self.drawAmmunition(player_ammo, player_max_ammo)
        self.isExitBarClicked()
        self.drawExitBar()
        return game_exited

    
# main menu bars
class MainMenuStartGameBar:
    def __init__(self):
        self.bar = menu_bar
        self.rect = self.bar.get_rect(center=(300, 300))
        self.text = font.render('START', False, 'Black')
        self.text_rect = self.text.get_rect(center=(300, 300))

    def isClicked(self):
        global game_activated, game_exited
        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]
        # if pressed start game
        if mouse_x >= 100 and mouse_x <= 500 and mouse_y >= 263 and mouse_y <= 338:
            pygame.draw.rect(screen, 'White', pygame.Rect(95, 258, 410, 85))

            if pygame.mouse.get_pressed()[0]:
                game_activated = True
                game_exited = False
        
        return game_activated

    def update(self):
        self.isClicked()
        screen.blit(self.bar, self.rect)
        screen.blit(self.text, self.text_rect)
        return game_activated


class MainMenuAnimatedLogo:
    def __init__(self):
        self.logo = font.render('SPACE SHOOTER', False, 'White')
        self.rect = self.logo.get_rect(center=(300, 100))

    def update(self):
        screen.blit(self.logo, self.rect)


class MainMenuExitBar:
    def __init__(self):
        self.bar = menu_bar
        self.rect = self.bar.get_rect(center=(300, 400))
        self.text = font.render('EXIT', False, 'Black')
        self.text_rect = self.text.get_rect(center=(300,400))

    def isClicked(self):

        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]
        # if exit bar get pressed quit the game
        if mouse_x >= 100 and mouse_x <= 500 and mouse_y >= 363 and mouse_y <= 438:
            pygame.draw.rect(screen, 'White', pygame.Rect(95, 358, 410, 85))

            if pygame.mouse.get_pressed()[0]:
                pygame.quit()
                sys.exit(0)

    def update(self):
        self.isClicked()
        screen.blit(self.bar, self.rect)
        screen.blit(self.text, self.text_rect)
