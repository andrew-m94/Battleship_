from game_board import Game_Board
from ships import Ships
from string import ascii_uppercase

class Player:

    def __init__(self, name):
        self.name = name
        self.ships = []
        self.create_ships()
        self.game_board = Game_Board()
        self.hidden_board = Game_Board()

    def create_ships(self):

        ship_one = Ships('destroyer', 2, 'D')
        self.ships.append(ship_one)

        ship_two = Ships('submarine', 3, 'S')
        self.ships.append(ship_two)

        ship_three = Ships('battleship one', 4, 'B')
        self.ships.append(ship_three)

        ship_four = Ships('battleship two', 4, 'B')
        self.ships.append(ship_four)

        ship_five = Ships('aircraft carrier', 5, '')
        self.ships.append(ship_five)

    def letters_to_numbers(self, location):
        letters_to_numbers = {}

        for count in range(1,21):
            letters_to_numbers[ascii_uppercase[count - 1]] = count

        location.split('')
        location[0] = letters_to_numbers[location[0]]
        location[1] = int(location[1])

        return location
            

    def place_ships(self):
        letters_to_numbers = self.letters_to_numbers()

        print('When placing ships, the ship will fill the spaces to the left (Horizontal) or above (vertical)')
        self.hidden_board.show_board()

        # for ship in self.ships:
        #     location = input(f'Enter a location (ie "A1") for your {ship.name} (size {ship.size}): ')
        #     converted_location = self.letters_to_numbers(location)
        #     #in work
