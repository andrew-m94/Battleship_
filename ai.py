from player import Player
import random

class Ai(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.miss = 0
        self.hit = 0
        self.row = 0
        self.column = 0
        self.choice = 0
        self.choice_list = [1,2,3,4,5]

    def place_ships(self):

        print(f'\n{self.name} is going to place their ships!')
        input('Press enter to continue: ')

        self.hidden_board.show_board()
        user_input_options = self.generate_user_options()
        
        for ship in self.ships:
            location = 'X'

            while location not in user_input_options:
                orientation = 0

                while location not in user_input_options:
                    print(f'Enter a location (ie "A1") for your {ship.name} (size {ship.size}): ')
                    location = self.auto_array_pick()

                while orientation != '1' and orientation != '2':
                    print('1: horizontal (to the left) \n2: vertical (up)\n Enter 1 or 2: ')
                    orientation = self.auto_orientation()

                location = self.validate_placement(location, orientation, ship)
                if location == None:
                    location = 'A1'

    def auto_array_pick(self):
        auto_array_options = self.generate_user_options()
        max_range = len(auto_array_options)
        rand_num = random.randrange(0,max_range)
        rand_input = auto_array_options[rand_num]

        return rand_input

    def auto_orientation(self):
        orientation = random.randrange(1,3)

        return str(orientation)