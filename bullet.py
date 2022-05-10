import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Creating a rectangle at (0,0) and setting its start posistion at the top center of our spaceship
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.spaceship.rect.midtop  

        self.y = float(self.rect.y)  # tracking the vertical position of the bullet

    # Moving and updating the position of the bullet
    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    # Telling the program to draw a bullet
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
