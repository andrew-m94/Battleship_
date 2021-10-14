from game_board import Game_Board
from ships import Ships


class Player:

    def __init__(self, name):
        self.name = name
        self.game_board = Game_Board()
        self.ships = []

    def create_ships(self):
        pass

    def place_ships(self):
        pass