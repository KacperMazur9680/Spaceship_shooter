class Game_stats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False  # Game is inactive at starting moment
        self.high_score = 0  

    # Which statistics are reset
    def reset_stats(self):
        self.spaceship_left = self.settings.spaceship_limit
        self.score = 0
        self.level = 1