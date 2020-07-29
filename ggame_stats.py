class GameStats():

    def __init__(self,a_setting):
        self.a_setting=a_setting
        self.reset_stats()
    def reset_stats(self):
        self.ships_left=self.a_setting.ship_limit
