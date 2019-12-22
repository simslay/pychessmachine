from game.pieces.piece import Piece

class King(Piece):
    x = None
    y = None
    
    def __init__(self, alliance):
        self.alliance = alliance
    
    def __repr__(self):
        return "K" if self.alliance == "Blacks" else "k"