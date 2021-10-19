from Battleship.game_board import Game_Board
from human import Human
from ai import Ai
from player import Player
from string import ascii_uppercase

class Play_Field:

    def __init__(self):
        self.player_one = None
        self.player_two = None
        self.run_game()

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

    def game_mode(self):
        choices = ['1','2','3']
        choice = 0

        print('1. Human vs Human (Grab a friend)')
        print('2. Human vs Ai (Can you beat a computer?)')
        print('3. Ai vs Ai (sit back and watch a game)')

        while choice not in choices:
            choice = input ('Choose your game mode: ')

        if choice == 1:
            self.player_one = Human()
            self.player_two = Human()

        if choice == 2:
            self.player_one = Human()
            self.player_two = Ai('Admiral AI')

        if choice == 3:
            self.player_one = Ai('Admiral AI')
            self.player_two = Ai('Admiral Ackbar')

    def player_one_turn(self):

        print(f"{self.player_one.name}'s turn!")
        input('Press enter to continue: ')

        print('Heres a damage report since last turn!')
        self.player_one.hidden_board.show_board()
        input('Press enter to continue: ')

        self.player_two.game_board.show_board()
        print(f'{len(self.player_one.ships)} ships remaining!')

        user_input_options = self.player_one.generate_user_options()
        attack = 'X'

        while attack not in user_input_options:
            if self.player_one == Human:
                attack = input('Enter a location ie "A1" to attack: ')
            else:
                attack = self.player_one.auto_array_pick()

        converted_location = self.letters_to_numbers(attack)
        row = converted_location[0]
        column = converted_location[1]

        if self.player_two.hidden_board.game_board[row][column] == '[ ]':
            self.player_two.hidden_board.game_board[row][column] = '[O]'
            self.player_two.game_board.game_board[row][column] = '[O]'
            print('Attack missed!')

        else:
            ship_hit = self.player_two.hidden_board.game_board[row][column]
            for ship in self.player_two.ships:
                if ship.symbol == ship_hit[1]:
                    ship.size -= 1
                    if ship.size == 0:
                        self.player_two.ships.remove(ship)
                        print(f"You sunk {self.player_two.name}'s {ship.name}")
                    else:
                        print(f"You hit {self.player_two.name}'s {ship.name}")
                    
            self.player_two.hidden_board.game_board[row][column] = '[X]'
            self.player_two.game_board.game_board[row][column] = '[X]'
            
        self.player_two.game_board.show_board()

    def player_two_turn(self):
        print(f"{self.player_two.name}'s turn!")
        input('Press enter to continue: ')

        print('Heres a damage report since last turn!')
        self.player_two.hidden_board.show_board()
        input('Press enter to continue: ')

        self.player_one.game_board.show_board()
        print(f'{len(self.player_one.ships)} ships remaining!')

        user_input_options = self.player_two.generate_user_options()
        attack = 'X'
        
        while attack not in user_input_options:

            if self.player_two == Human:
                attack = input('Enter a location ie "A1" to attack: ')
            else:
                attack = self.player_two.auto_array_pick()

        converted_location = self.letters_to_numbers(attack)
        row = converted_location[0]
        column = converted_location[1]

        if self.player_one.hidden_board.game_board[row][column] == '[ ]':
            self.player_one.hidden_board.game_board[row][column] = '[O]'
            self.player_one.game_board.game_board[row][column] = '[O]'
            print('Attack missed!')

        else:
            ship_hit = self.player_one.hidden_board.game_board[row][column]

            for ship in self.player_one.ships:

                if ship.symbol == ship_hit[1]:
                    ship.size -= 1

                    if ship.size == 0:
                        self.player_one.ships.remove(ship)
                        print(f"You sunk {self.player_one.name}'s {ship.name}")

                    else:
                        print(f"You hit {self.player_one.name}'s {ship.name}")
                    
            self.player_one.hidden_board.game_board[row][column] = '[X]'
            self.player_one.game_board.game_board[row][column] = '[X]'
    
        self.player_one.game_board.show_board()

    def ai_attack_pattern(self):

    def rounds_of_play(self):

        while len(self.player_one.ships) > 0 and len(self.player_two.ships) > 0:
            self.player_one_turn()

            if len(self.player_two.ships) > 0:
                self.player_two_turn()

    def run_game(self):
        self.intro()
        self.game_mode
        self.player_one.place_ships()
        self.player_two.place_ships()
        self.rounds_of_play()
        self.display_winner()

    def intro(self):
        print('\nWelcome to Battleship!')
        print('Players will each place ships in the water and take turns attacking each other until either ' +
        'player has no ships remaining.')
        print('Have fun!')

    def display_winner(self):
        if len(self.player_two.ships) == 0:
            print(f'{self.player_one.name} wins!')
        
        elif len(self.player_one.ships) == 0:
            print(f'{self.player_two.name} wins!')