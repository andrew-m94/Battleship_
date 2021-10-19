from player import Player

class Ai(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def place_ships(self):
        pass