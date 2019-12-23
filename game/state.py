from game.pieces.bishop import Bishop
from game.pieces.king import King
from game.pieces.knight import Knight
from game.pieces.pawn import Pawn
from game.pieces.queen import Queen
from game.pieces.rook import Rook
from game.pieces.piece import Piece

class State():
    board = []
    white_pieces = None
    black_pieces = None
    white_captures = [] # black pieces
    black_captures = [] # white pieces
    player = None
    move = ""
    white_king = None
    black_king = None
    check = False
    
    def __init__(self):
        self.board = [[Rook("Blacks"), Knight("Blacks"), Bishop("Blacks"), Queen("Blacks"), King("Blacks"), Bishop("Blacks"), Knight("Blacks"), Rook("Blacks")],
                      [Pawn("Blacks"), Pawn("Blacks"), Pawn("Blacks"), Pawn("Blacks"), Pawn("Blacks"), Pawn("Blacks"), Pawn("Blacks"), Pawn("Blacks")],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [Pawn("Whites"), Pawn("Whites"), Pawn("Whites"), Pawn("Whites"), Pawn("Whites"), Pawn("Whites"), Pawn("Whites"), Pawn("Whites")],
                      [Rook("Whites"), Knight("Whites"), Bishop("Whites"), Queen("Whites"), King("Whites"), Bishop("Whites"), Knight("Whites"), Rook("Whites")]]
        
        self.white_pieces = [self.board[7][0], self.board[7][1], self.board[7][2], self.board[7][3],
                         self.board[7][4], self.board[7][5], self.board[7][6], self.board[7][7],
                         self.board[6][0], self.board[6][1], self.board[6][2], self.board[6][3],
                         self.board[6][4], self.board[6][5], self.board[6][6], self.board[6][7]]
        
        self.black_pieces = [self.board[0][0], self.board[0][1], self.board[0][2], self.board[0][3],
                         self.board[0][4], self.board[0][5], self.board[0][6], self.board[0][7],
                         self.board[1][0], self.board[1][1], self.board[1][2], self.board[1][3],
                         self.board[1][4], self.board[1][5], self.board[1][6], self.board[1][7]]
        
        for x in range(8):
            for y in range(8):
                if self.board[x][y] != None:
                    self.board[x][y].x = x
                    self.board[x][y].y = y
    
    def printBoard(self):
        count = 0
        for x in range(8):
            for y in range(8):
                if self.board[x][y] != None:
                    print('|', end=str(self.board[x][y]))
                else:
                    print('|', end='-')
                count += 1
                if count == 8:
                    print('|', end='\n')
                    count = 0
    
    def add_capture(self, piece):
        if piece.alliance == "Whites":
            self.black_captures.append(piece)
        elif piece.alliance == "Blacks":
            self.white_captures.append(piece)
