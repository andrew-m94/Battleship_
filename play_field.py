from player import Player

class Play_Field:

    def __init__(self):
        self.player = Player()
        self.run_game()

    def player_one_turn(self):
        pass

    def player_two_turn(self):
        pass

    def round_of_play(self):
        self.player_one_turn()
        self.player_two_turn()

    def run_game(self):
        self.intro()
        self.player.place_ships()
        self.round_of_play()
        self.display_winner()

    def intro(self):
        pass

    def display_winner(self):
        pass