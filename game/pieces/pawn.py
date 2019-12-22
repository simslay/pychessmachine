from game.pieces.piece import Piece

class Pawn(Piece):
    x = None
    y = None
    
    def __init__(self, alliance):
        self.alliance = alliance
    
    def __repr__(self):
        return "P" if self.alliance == "Blacks" else "p"