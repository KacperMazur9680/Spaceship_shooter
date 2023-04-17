from pygame.sprite import Sprite
import pygame

class Lives(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/Pixel_ship.png')  # image of lives
        self.rect = self.image.get_rect()  # setting the image as a rectangle
