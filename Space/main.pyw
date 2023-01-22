from settings import *
from player import Player
from background import AnimatedBackground
from menu import MainMenu, game_activated
from bars import HudGameLowBar
from enemies import *

invader_timer = pygame.USEREVENT + 1
pygame.time.set_timer(invader_timer, 1000)

invaders_size = 0
enemies_killed = 0

enemies_killed_surf = font2.render('ENEMIES KILLED: ', False, 'Black').convert()

# main loop
if __name__ == '__main__':
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == invader_timer:
                invaders.add(SpaceInvader(randint(25, 575)))
                invaders_size += 1

        if game_activated:
            background.update()
            invaders.draw(screen)

            invaders.update(player.bullet_list)
            if invaders_size > len(invaders):
                enemies_killed += 1
                invaders_size -= 1
            
            if lowbar.update(player.ammo, player.max_ammo):
                game_activated = False

            player.update(invaders)
            enemies_killed_count = font2.render(f'{enemies_killed}', False, 'Black').convert()
            screen.blit(enemies_killed_surf, (10, 760))
            screen.blit(enemies_killed_count, (200, 760))

        else:
            enemies_killed = 0
            invaders_size = 0
            player = Player()
            background = AnimatedBackground()
            main_menu = MainMenu()
            lowbar = HudGameLowBar()
            invaders = pygame.sprite.Group() # clearing the group

            
            game_activated = main_menu.update()


        pygame.display.update()
        clock.tick(FPS)

