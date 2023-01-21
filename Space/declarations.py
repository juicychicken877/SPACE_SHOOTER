from settings import *

# backgrounds
background_1 = pygame.image.load('images/backgrounds/space-background-1.jpg').convert_alpha()
background_black1 = pygame.image.load('images/backgrounds/space-background-2-black.jpg').convert_alpha()
background_black2 = background_black1

# player
player_image = pygame.image.load('images/.xcf/ship-1.xcf').convert_alpha()

# sounds
shoot = pygame.mixer.Sound('sounds/shoot.wav')
shoot.set_volume(0.1)

# bullet
bullet = pygame.image.load('images/default/bullet-red.png').convert_alpha()

# menu bars
menu_bar = pygame.image.load('images/default/menu_bar.png')
