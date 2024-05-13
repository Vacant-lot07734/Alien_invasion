class Settings:
    """存储所有设置类"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # loc of the ship
        self.ship_speed_factor = 0.5

        # setting of bullets
        self.bullet_speed_factor = 0.3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 6

        # setting of aliens
        self.alien_speed_factor = 0.2
        self.fleet_drop_speed = 5
        # 1 right, -1 left
        self.fleet_direction = 1
