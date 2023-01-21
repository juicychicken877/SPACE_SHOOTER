from declarations import background_black1, background_black2
from settings import screen


class AnimatedBackground:
    def __init__(self):
        self.image1 = background_black1
        self.image2 = background_black2

        self.image1_rect = self.image1.get_rect(topleft=(0,0))
        self.image2_rect = self.image2.get_rect(topleft=(0,-1250))

        self.y1 = 0
        self.y2 = -1250

        self.speed = 3

    def move(self):
        self.image1_rect.y += self.speed
        self.image2_rect.y += self.speed

        if self.image1_rect.y >= 1250:
            self.image1_rect.y = -1250

        elif self.image2_rect.y >= 1250:
            self.image2_rect.y = -1250

    def update(self):
        # draw
        self.move()
        screen.blit(self.image1, self.image1_rect)
        screen.blit(self.image2, self.image2_rect)