import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for i in range(3):
            print('|'.join(self.board[i*3:(i+1)*3]))
            if i < 2:
                print('-' * 5)

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

    def play_game(self):
        print("Ducks (X) vs Hippos (O)")
        letter = 'X'
        while self.empty_squares():
            if self.current_winner:
                print(f"{self.current_winner} wins!")
                return
            if letter == 'X':
                square = int(input(f"Ducks' turn. Choose a square (0-8): "))
            else:
                square = random.choice(self.available_moves())
                print(f"Hippos' turn. Chose square {square}.")
            if self.make_move(square, letter):
                self.print_board()
                letter = 'O' if letter == 'X' else 'X'
        print("It's a tie!")

if __name__ == '__main__':
    game = TicTacToe()
    game.play_game()
