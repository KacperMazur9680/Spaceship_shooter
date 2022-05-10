class Settings:
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.spaceship_limit = 3  # number of lives

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3  # how many bullets can be on the screen at once

        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1  # how much faster the targets after every level
        self.score_scale = 1.5  # by how much the targes value increases

        self.initialize_dynamic_settings()

    # Changes initialized throughout the game
    def initialize_dynamic_settings(self):
        self.spaceship_speed = 1.5
        self.bullet_speed = 2.0
        self.target_speed = 0.5
        self.fleet_direction = 1  # 1 = fleet going right, -1 = fleet going left
        self.target_points = 50

    # Incresing the difficulty 
    def increase_speed(self):
        self.spaceship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.target_speed *= self.speedup_scale

        self.target_points = int(self.target_points * self.score_scale)  # increasing earned points for shooting down a target
