class Color:
    EMPTY = 0
    BLACK = 1
    WHITE = 2


class Empty:
    color = Color.EMPTY

    def get_moves(self, board, x, y):
        raise Exception('$)$_404_$)$')

    def __repr__(self):
        return '.'


class ChessMan:
    IMG = None

    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return self.IMG[0 if self.color == Color.WHITE else 1]


class Pawn(ChessMan):
    IMG = ('♟', '♙')

    def get_moves(self, board, x, y):
        moves = []
        if self.color == Color.BLACK and y < 7 and board.get_color(x, y + 1) == Color.EMPTY:
            moves.append([x, y + 1])
        elif self.color == Color.WHITE and y > 0 and board.get_color(x, y - 1) == Color.EMPTY:
            moves.append([x, y - 1])
        return moves


class Queen(ChessMan):
    IMG = ('♛', '♕')


class King(ChessMan):
    IMG = ('♚', '♔')

    def get_moves(self, board, x, y):
        moves = []
        if self.color == Color.BLACK and y < 7 and board.get_color(x, y + 1) == Color.EMPTY:
            moves.append([x, y + 1])
        elif self.color == Color.BLACK and y > 0 and board.get_color(x, y - 1) == Color.EMPTY:
            moves.append([x, y - 1])
        elif self.color == Color.BLACK and x < 7 and board.get_color(x + 1, y) == Color.EMPTY:
            moves.append([x + 1, y])
        elif self.color == Color.BLACK and y > 0 and board.get_color(x - 1, y) == Color.EMPTY:
            moves.append([x - 1, y])

        return moves


class Board:
    def __init__(self):
        self.board = [[Empty()] * 8 for y in range(8)]
        self.board[1][0] = Pawn(Color.BLACK)
        self.board[1][1] = Pawn(Color.BLACK)
        self.board[1][2] = Pawn(Color.BLACK)
        self.board[1][3] = Pawn(Color.BLACK)
        self.board[1][4] = Pawn(Color.BLACK)
        self.board[1][5] = Pawn(Color.BLACK)
        self.board[1][6] = Pawn(Color.BLACK)
        self.board[1][7] = Pawn(Color.BLACK)
        self.board[0][3] = King(Color.BLACK)
        self.board[0][4] = Queen(Color.BLACK)
        self.board[6][0] = Pawn(Color.WHITE)
        self.board[6][1] = Pawn(Color.WHITE)
        self.board[6][2] = Pawn(Color.WHITE)
        self.board[6][3] = Pawn(Color.WHITE)
        self.board[6][4] = Pawn(Color.WHITE)
        self.board[6][5] = Pawn(Color.WHITE)
        self.board[6][6] = Pawn(Color.WHITE)
        self.board[6][7] = Pawn(Color.WHITE)
        self.board[7][3] = King(Color.WHITE)
        self.board[7][4] = Queen(Color.WHITE)

    def get_color(self, x, y):
        return self.board[y][x].color

    def get_moves(self, x, y):
        return self.board[y][x].get_moves(self, x, y)

    def move(self, xy_from, xy_to):
        self.board[xy_to[1]][xy_to[0]] = self.board[xy_from[1]][xy_from[0]]
        self.board[xy_from[1]][xy_from[0]] = Empty()

    def __repr__(self):
        res = ''
        for y in range(8):
            res += ''.join(map(str, self.board[y])) + '\n'
        return res


b = Board()
print(b)
P2 = b.get_moves(1, 1)
b.move([1, 1], P2[0])
print(b)
P7 = b.get_moves(6, 6)
b.move([6, 6], P7[0])
print(b)
