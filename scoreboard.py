import pygame.font
from pygame.sprite import Group
from lives import Lives
import json
import os

class Scoreboard:
    def __init__(self, ai_game, username):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.username = username

        # Font settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_image()

    # Making the score a render image
    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Placing the score on the screen (top right)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    # Making the high score a render image
    def prep_high_score(self):

        # Storing the high score
        if not os.path.exists('high_scores_folder'):
                os.makedirs('high_scores_folder')
        
        folder = 'high_scores_folder'
        path = f'{self.username}_high_score.json'
        
        self.file_path = os.path.join(folder, path)
        # check if file with said name exists
        if os.path.exists(self.file_path):
            pass
        else:
            # create a file
            with open(self.file_path, 'w') as fp:
                json.dump(0, fp)

        # read users highest score
        with open(self.file_path) as f:
            self.high_score_stored = json.load(f)

        high_score_str = "{:,}".format(self.high_score_stored)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Placing the high score on the screen (top center)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    # Drawing the score on the screen
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.lives.draw(self.screen)

    # Checking for a new high score
    def check_high_score(self):
        if self.stats.score > self.high_score_stored:
            self.stats.high_score = self.stats.score

            # Editing the stored high score
            with open(self.file_path, "w") as f:
                json.dump(self.stats.high_score, f)
            self.prep_high_score()

    # Making the level a render image
    def prep_level(self):
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # Placing the level on the screen (under the score)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    # Showing the number of lives 
    def prep_lives(self):
        self.lives = Group()
        for spaceship_number in range(self.stats.spaceship_left):
            spaceship = Lives(self.ai_game)
            spaceship.rect.x = 10 + spaceship_number * spaceship.rect.width
            spaceship.rect.y = 5
            self.lives.add(spaceship)

    # Calling for every information
    def prep_image(self):
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_lives()