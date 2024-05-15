# assignment: programming assignment 5
# author: (Emiliano Bustos)
# date: (December 7, 2023)
# file: chess.py is a program that displays valid moves of chess pieces
# input: (user input to where the chess piece is placed)
# output: (display valid moves according to position of chess piece input)
#THIS IS ME IN MAY 2024
class Board: 
    def __init__(self):
        self.board = {}
        self.empty()

    def empty(self):
        for col in 'abcdefgh':
            for row in '12345678':
                self.board[col + row] = ' '
        

    def set(self, pos, piece):
        if pos in self.board.keys():
            self.board[pos] = piece
    
    def get_keys(self):
        return self.board.keys()

    def draw(self):
        print("   a   b   c   d   e   f   g   h")
        print(" +---+---+---+---+---+---+---+---+")

        for row in '87654321':
            row_str = row + '|'
            for col in 'abcdefgh':
                piece = self.board[col + row]
                row_str += f" {piece} |"
            print(row_str + '' + row)
            print(" +---+---+---+---+---+---+---+---+")

        print("   a   b   c   d   e   f   g   h")


class Chess_Piece:
    def __init__(self, board, pos, color='white'):
        self.position = self.get_index(pos)
        self.color = color
        board.set(pos, self.get_name())
    def get_index(self, pos):
        return ('abcdefgh'.index(pos[0]), '12345678'.index(pos[1]))
    def get_name(self):
        pass
    def moves(self, board):
        pass


class King(Chess_Piece):
    #insert code
    def get_name(self):
        return 'K'
    def moves(self, board):
        for key in board.get_keys():
                key_index = self.get_index(key)
                if key_index == self.position:
                    continue
                elif key_index[0] in (self.position[0] - 1, self.position[0], self.position[0] + 1) and \
                        key_index[1] in (self.position[1] - 1, self.position[1], self.position[1] + 1):
                    board.set(key, 'x')


class Queen(Chess_Piece):
    def get_name(self):
        return 'Q'
    def moves(self, board):
        for key in board.get_keys():
            key_index = self.get_index(key)
            if key_index == self.position:
                continue
            elif key_index[0] == self.position[0]:
                board.set(key, 'x')
            elif key_index[1] == self.position[1]:
                board.set(key, 'x')
            elif key_index == self.position:
                continue
            elif (key_index[0] - self.position[0]) == (key_index[1] - self.position[1]) or (key_index[0] - self.position[0]) == (self.position[1] - key_index[1]):
                board.set(key, "x")

class Rook(Chess_Piece):
    def get_name(self):
        return 'R'
    def moves(self, board):
        for key in board.get_keys():
            key_index = self.get_index(key)
            if key_index == self.position:
                continue
            elif key_index[0] == self.position[0]:
                board.set(key, 'x')
            elif key_index[1] == self.position[1]:
                board.set(key, 'x')

class Knight(Chess_Piece):
    def get_name(self):
        return 'N'
    def moves(self, board):
        for key in board.get_keys():
            key_index = self.get_index(key)
            if key_index == self.position:
                continue
            elif (key_index[0] == self.position[0] + 1 and key_index[1] == self.position[1] + 2) or \
                 (key_index[0] == self.position[0] + 1 and key_index[1] == self.position[1] - 2) or \
                 (key_index[0] == self.position[0] - 1 and key_index[1] == self.position[1] + 2) or \
                 (key_index[0] == self.position[0] - 1 and key_index[1] == self.position[1] - 2) or \
                 (key_index[0] == self.position[0] + 2 and key_index[1] == self.position[1] + 1) or \
                 (key_index[0] == self.position[0] + 2 and key_index[1] == self.position[1] - 1) or \
                 (key_index[0] == self.position[0] - 2 and key_index[1] == self.position[1] + 1) or \
                 (key_index[0] == self.position[0] - 2 and key_index[1] == self.position[1] - 1):
                board.set(key, 'x')

class Bishop(Chess_Piece):
    def get_name(self):
        return 'B'
    def moves(self, board):
        for key in board.get_keys():
            key_index = self.get_index(key)
            if key_index == self.position:
                continue
            elif (key_index[0] - self.position[0]) == (key_index[1] - self.position[1]) or (key_index[0] - self.position[0]) == (self.position[1] - key_index[1]):
                board.set(key, "x")


#main code
if __name__ == '__main__':
    print("Welcome to the Chess Game!\n Get ready to play. ♟️")
    board = Board()
    board.draw()
    while True:
        choice = input("Enter a chess piece and its position or type X to exit:\n").lower()
        if choice == 'x':
            print("Goodbye!")
            break
        elif len(choice) != 3:
            continue
        elif choice[0] not in 'kqrbn' or choice[1] not in 'abcdefgh' or choice[2] not in '12345678':
            continue
        elif choice[0] == 'r':
            rook = Rook(board, choice[1:])
            rook.moves(board)
        elif choice[0] == 'k':
            king = King(board, choice[1:])
            king.moves(board)
        elif choice[0] == 'q':
            queen = Queen(board, choice[1:])
            queen.moves(board)
        elif choice[0] == 'n':
            knight = Knight(board, choice[1:])
            knight.moves(board)
        elif choice[0] == 'b':
            bishop = Bishop(board, choice[1:])
            bishop.moves(board)

        board.draw()
        board.empty()

