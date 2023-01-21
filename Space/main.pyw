import sys
from settings import *
from declarations import *
from player import Player
from background import AnimatedBackground
from menu import MainMenu


game_active = True

pygame.display.set_caption(WINDOW_TITLE)

player = Player()
background = AnimatedBackground()
main_menu = MainMenu()

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if game_active:
        background.update()
        player.update()

    else:
        main_menu.draw()

    pygame.display.update()
    clock.tick(FPS)

