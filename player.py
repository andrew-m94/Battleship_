from game_board import Game_Board
from ships import Ships


class Player:

    def __init__(self, name):
        self.name = name
        self.ships = []
        self.create_ships()
        self.game_board = Game_Board()

    def create_ships(self):

        ship_one = Ships('destroyer', 2)
        self.ships.append(ship_one)

        ship_two = Ships('submarine', 3)
        self.ships.append(ship_two)

        ship_three = Ships('battleship one', 4)
        self.ships.append(ship_three)

        ship_four = Ships('battleship two', 4)
        self.ships.append(ship_four)

        ship_four = Ships('battleship two', 4)
        self.ships.append(ship_four)

        ship_five = Ships('aircraft carrier', 5)
        self.ships.append(ship_five)

    def place_ships(self):
        pass