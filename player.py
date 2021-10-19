from game_board import Game_Board
from ships import Ships
from string import ascii_uppercase

class Player:

    def __init__(self):
        self.name = ''
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

        element = 0
        numbers = 1

        return user_input_options

    def place_ships(self):
        pass

    def validate_placement(self, location, orientation, ship):
            
        converted_location = self.letters_to_numbers(location)
        row = converted_location[0]
        column = converted_location[1]
        #Converts user input. A1 = 1 1, B10 = 2 10, etc for array call 

        if int(orientation) == 1:

            if ship.size <= column:
                check_column = column

            else:
                print('Your Ship does not fit there!')
                location = 'X'
                return location

            for count in range(ship.size):

                    if self.hidden_board.game_board[row][check_column] == '[ ]':
                        check_column -= 1
                        error_check = False
                    else:
                        print('Another ship is in the way!')
                        location = 'X'
                        return location
                    
            for count in range(ship.size):
                self.hidden_board.game_board[row][column] = f'[{ship.symbol}]'
                column -= 1

            self.hidden_board.show_board()

        elif int(orientation) == 2:

            if ship.size <= row:
                check_row = row
            
            else:
                print('Your Ship does not fit there!')
                location = 'X'
                return location

            for count in range(ship.size):
                        
                if self.hidden_board.game_board[check_row][column] == '[ ]':
                        check_row -= 1

                else:
                        print('Another ship is in the way!')
                        location = 'X'
                        return location

            for count in range(ship.size):
                self.hidden_board.game_board[row][column] = f'[{ship.symbol}]'
                row -= 1

            self.hidden_board.show_board()