from string import ascii_uppercase

class Game_Board:
    
    def __init__(self):
        self.create_board()

    def create_board(self):
        game_board = [['[ ]' for columns in range(21)]for row in range(21)]

        game_board[0][0] = ' '

        for count in range(1,21):
            char = ascii_uppercase[count - 1]
            game_board[count][0] = char

        for count in range(1,10):
            game_board[0][count] = f' {count} '

        for count in range(10,21):
            game_board[0][count] = f'{count} '

    def show_board(self, board_name):

        for rows in board_name:
            for element in rows:
                print(element, end = ' ')
            print('')
