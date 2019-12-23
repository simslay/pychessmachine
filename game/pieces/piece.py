from abc import abstractmethod

class Piece():
    alliance = None
    promoted = False
    castling_poss = True
    nom = None
    
    def __init__(self):
        pass
    
    @abstractmethod
    def is_valid_move(self, x1, y1, x2, y2, board, player, check):
        if x1 == x2 and y1 == y2:
            return False
        if not (self.alliance == player.alliance and
             ((board[y2][x2] != None and board[y2][x2].alliance != self.alliance) or
              board[y2][x2] == None)):
            return False