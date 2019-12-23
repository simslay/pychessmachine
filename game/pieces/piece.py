from abc import abstractmethod

class Piece():
    alliance = None
    promoted = False
    castling_poss = True
    nom = None
    en_passant_risk = False
    
    def __init__(self):
        pass
    
    @abstractmethod
    def is_valid_move(self, x1, y1, x2, y2, board, player, check):
        pass
