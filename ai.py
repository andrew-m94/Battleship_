from player import Player
import random

class Ai(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def place_ships(self):
        pass

    def auto_array_pick(self):
        auto_array_options = self.generate_user_options()
        max_range = len(auto_array_options)
        rand_num = random.randrange(0,max_range)
        rand_input = auto_array_options[rand_num]

        return rand_input

    def auto_orientation(self):
        orientation = random.randrange(1,3)

        return orientation