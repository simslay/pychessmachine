from game.pieces.piece import Piece

class Rook(Piece):
    x = None
    y = None
    
    def __init__(self, alliance):
        self.alliance = alliance
    
    def __repr__(self):
        return "R" if self.alliance == "Blacks" else "r"