from game_board import Game_Board
from ships import Ships
from string import ascii_uppercase

class Player:

    def __init__(self):
        self.name = ''
        self.add_name()
        self.ships = []
        self.create_ships()
        self.game_board = Game_Board()
        self.hidden_board = Game_Board()

    def add_name(self):
        self.name = input('Enter a name for each player one at a time: ')

    def create_ships(self):

        ship_one = Ships('destroyer', 2, 'D')
        self.ships.append(ship_one)

        ship_two = Ships('submarine', 3, 'S')
        self.ships.append(ship_two)

        ship_three = Ships('battleship one', 4, 'B')
        self.ships.append(ship_three)

        ship_four = Ships('battleship two', 4, 'b')
        self.ships.append(ship_four)

        ship_five = Ships('aircraft carrier', 5, 'A')
        self.ships.append(ship_five)

    def letters_to_numbers(self, location):
        letters_to_numbers = {}

        for count in range(1,21):
            letters_to_numbers[ascii_uppercase[count - 1]] = count

        location = list(location)
        
        if len(location) > 2:
            location[1] = f'{location[1]}{location[2]}'
        
        location[0] = letters_to_numbers[location[0].upper()]
        location[1] = int(location[1])

        return location

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

        return user_input_options
        
    def place_ships(self):

        print(f'\n{self.name} place your ships!')
        input('Press enter to continue: ')

        print('\nWhen placing ships, the ship will fill the spaces to the left (Horizontal) or above (vertical)')
        self.hidden_board.show_board()

        for ship in self.ships:
            location = input(f'Enter a location (ie "A1") for your {ship.name} (size {ship.size}): ')

    def validate_placement(self, location, ship):
            
        converted_location = self.letters_to_numbers(location)
        row = converted_location[0]
        column = converted_location[1]

        error_check = True
        while error_check == True:
            orientation = input('1: horizontal (to the left) \n2: vertical (up)\n Enter 1 or 2: ')

            if int(orientation) == 1:
                if ship.size <= column:
                        check_column = column

                for count in range(ship.size):

                        if self.hidden_board.game_board[row][check_column] == '[ ]':
                            check_column -= 1
                            error_check = False
                        else:
                            print('Another ship is in the way!\n')
                            error_check = True
                            break
                        
                if error_check == False:
                    for count in range(ship.size):
                        self.hidden_board.game_board[row][column] = f'[{ship.symbol}]'
                        column -= 1

                    self.hidden_board.show_board()
                    
                else:
                    print('Your Ship does not fit there!')

            elif int(orientation) == 2:
                if ship.size <= row:
                    check_row = row

                    for count in range(ship.size):
                            
                        if self.hidden_board.game_board[check_row][column] == '[ ]':
                            check_row -= 1
                            error_check = False
                        else:
                            print('Another ship is in the way!\n')
                            error_check = True
                            break
                        
                    if error_check == False:
                        for count in range(ship.size):
                            self.hidden_board.game_board[row][column] = f'[{ship.symbol}]'
                            row -= 1

                        self.hidden_board.show_board()

                else:
                    print('Your Ship does not fit there!')