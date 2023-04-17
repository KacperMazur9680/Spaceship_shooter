import pygame
from pygame.sprite import Sprite

class Spaceship(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/Pixel_ship.png')  # image of the spaceship
        self.rect = self.image.get_rect()  # setting the image as a rectangle
        self.rect.midbottom = self.screen_rect.midbottom  # starting point of the spaceship (bottom center)
        self.x = float(self.rect.x)  # tracking the horizontal position of the spaceship
        self.y = float(self.rect.y)  # tracking the vertical position of the spaceship

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    # Centering the spaceship
    def center_spaceship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    # Updating the position of the spaceship
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.spaceship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.spaceship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.spaceship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.spaceship_speed
        self.rect.x = self.x
        self.rect.y = self.y

    # Drawing the spaceship at its current location
    def blitme(self):
        self.screen.blit(self.image, self.rect)
