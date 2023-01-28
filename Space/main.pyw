from settings import *
from player import Player
from background import AnimatedBackground
from menu import MainMenu, game_activated
from bars import HudGameLowBar
from enemies import *

invader_timer = pygame.USEREVENT + 1
pygame.time.set_timer(invader_timer, 500)

invaders_size = 0
score = 0
score_text = font3.render('SCORE', False, 'Black')

# main loop
if __name__ == '__main__':
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == invader_timer:
                invaders.add(SpaceInvader(randint(50, 550), choice(['green', 'blue', 'purple'])))
                invaders_size += 1

        if game_activated:
            background.update()
            invaders.draw(screen)
            invaders.update(player.bullet_list)
    
            # if invader got killed
            if len(invaders) < invaders_size:
                score += 100
                invaders_size -= 1

            if lowbar.update(player.ammo, player.max_ammo):
                game_activated = False

            player.update(invaders)

            score_count = font3.render(f'{score}', False, 'Black')
            # score bar
            screen.blit(score_count, (225, 760))
            screen.blit(score_text, (225, 725))
        else:
            invaders_size = 0
            score = 0
            
            player = Player()
            background = AnimatedBackground()
            main_menu = MainMenu()
            lowbar = HudGameLowBar()
            invaders = pygame.sprite.Group() # clearing the group

            
            game_activated = main_menu.update()


        pygame.display.update()
        clock.tick(FPS)

