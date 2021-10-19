from player import Player
from string import ascii_lowercase
from string import ascii_uppercase

class Human(Player):
    def __init__(self):
        super().__init__()
        self.add_name()

    def add_name(self):
        self.name = input('Enter a name for each player one at a time: ')

    def generate_user_options(self):
        user_input_options = []
        element = 0
        numbers = 1

        for letter in ascii_uppercase[0:20]:
            for count in range (1,21):
                user_input_options.append(f'{ascii_uppercase[element]}{numbers}')
                numbers += 1
            numbers = 1
            element += 1

        element = 0
        numbers = 1

        for letter in ascii_lowercase[0:20]:
            for count in range (1,21):
                user_input_options.append(f'{ascii_lowercase[element]}{numbers}')
                numbers += 1
            numbers = 1
            element += 1

        return user_input_options

    def place_ships(self):

        print(f'\n{self.name} place your ships!')
        input('Press enter to continue: ')

        print('\nWhen placing ships, the ship will fill the spaces to the left (Horizontal) or above (vertical)')
        self.hidden_board.show_board()

        user_input_options = self.generate_user_options()
        
        for ship in self.ships:
            location = 'X'

            while location not in user_input_options:
                orientation = 0

                while location not in user_input_options:
                    location = input(f'Enter a location (ie "A1") for your {ship.name} (size {ship.size}): ')

                while orientation != '1' and orientation != '2':
                    orientation = input('1: horizontal (to the left) \n2: vertical (up)\n Enter 1 or 2: ')

                location = self.validate_placement(location, orientation, ship)
                if location == None:
                    location = 'A1'