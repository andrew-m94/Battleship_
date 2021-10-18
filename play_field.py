from player import Player
from string import ascii_uppercase

class Play_Field:

    def __init__(self):
        self.player_one = Player()
        self.player_two = Player()
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

    def player_one_turn(self):
        round = 0

        print(f"{self.player_one.name}'s turn!")
        input('Press enter to continue: ')

        if round > 0:
            print('Heres a damage report since last turn!')
            print(self.player_one.hidden_board.show_board())
            input('Press enter to continue: ')

        self.player_two.game_board.show_board()
        attack = input('Enter a location ie "A1" to attack: ')

        converted_location = self.letters_to_numbers(attack)
        row = converted_location[0]
        column = converted_location[1]

        if self.player_two.hidden_board[row][column] == '[ ]':
            self.player_two.hidden_board[row][column] = '[O]'
            print('Attack missed!')

        else:
            ship_hit = self.player_two.hidden_board[row][column]
            for ship in self.player_two.ships:
                if ship.symbol == ship_hit[1]:
                    ship.size -= 1
                    if ship.size == 0:
                        self.player_two.ships.remove(ship)
                        print(f"You sunk {self.player_two.name}'s {ship.name}")
                    else:
                        print(f"You hit {self.player_two.name}'s {ship.name}")
                    
            self.player_two.hidden_board[row][column] = '[X]'
            self.player_two.game_board[row][column] = '[X]'
            self.player_two.game_board.show_board()

        round += 0

    def player_two_turn(self):
        print(f"{self.player_two.name}'s turn!")
        input('Press enter to continue: ')

        print('Heres a damage report since last turn!')
        print(self.player_two.hidden_board.show_board())
        input('Press enter to continue: ')

        self.player_one.game_board.show_board()
        attack = input('Enter a location ie "A1" to attack: ')

        converted_location = self.letters_to_numbers(attack)
        row = converted_location[0]
        column = converted_location[1]

        if self.player_one.hidden_board[row][column] == '[ ]':
            self.player_one.hidden_board[row][column] = '[O]'
            self.player_one.game_board[row][column] = '[O]'
            print('Attack missed!')

        else:
            ship_hit = self.player_one.hidden_board[row][column]

            for ship in self.player_one.ships:

                if ship.symbol == ship_hit[1]:
                    ship.size -= 1

                    if ship.size == 0:
                        self.player_one.ships.remove(ship)
                        print(f"You sunk {self.player_one.name}'s {ship.name}")
                        
                    else:
                        print(f"You hit {self.player_one.name}'s {ship.name}")
                    
            self.player_one.hidden_board[row][column] = '[X]'
            self.player_one.game_board[row][column] = '[X]'
    
        self.player_one.game_board.show_board()

    def rounds_of_play(self):

        while len(self.player_one.ships) > 0 and len(self.player_two.ships) > 0:
            self.player_one_turn()

            if len(self.player_two.ships) > 0:
                self.player_two_turn()

    def run_game(self):
        self.intro()
        self.player_one.place_ships()
        self.player_two.place_ships()
        self.rounds_of_play()
        self.display_winner()

    def intro(self):
        print('\nWelcome to Battleship!')
        print('Players will each place ships in the water and take turns attacking each other until either ' +
        'player has no ships remaining.')
        print('Have fun!\n')

    def display_winner(self):
        if len(self.player_two.ships) == 0:
            print(f'{self.player_one.name} wins!')
        
        elif len(self.player_one.ships) == 0:
            print(f'{self.player_two.name} wins!')