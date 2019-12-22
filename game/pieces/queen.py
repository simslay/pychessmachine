from game.pieces.piece import Piece

class Queen(Piece):
    x = None
    y = None
    
    def __init__(self, alliance):
        self.alliance = alliance
    
    def __repr__(self):
        return "Q" if self.alliance == "Blacks" else "q"