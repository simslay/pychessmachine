from game.pieces.piece import Piece

class Knight(Piece):
    x = None
    y = None
    
    def __init__(self, alliance):
        self.alliance = alliance
    
    def __repr__(self):
        return "N" if self.alliance == "Blacks" else "n"