import pygame
from pygame.sprite import Sprite

# A class for showing on the screen a target
class Target(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load("images/silly.png")  # image of the target
        self.rect = self.image.get_rect()  # setting the image as a rectangle

        self.rect.x = self.rect.width  # space between targets equal to the width of one target
        self.rect.y = self.rect.height # space above targets equal to the height of one target
        self.x = float(self.rect.x)  # tracking the horizontal position of a target

    # Information for the program if an target has touched an edge of the display window
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    # Deciding which way to move the target
    def update(self):
        self.x += (self.settings.target_speed * self.settings.fleet_direction)
        self.rect.x = self.x  # updating its position

