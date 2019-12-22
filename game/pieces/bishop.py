from game.pieces.piece import Piece

class Bishop(Piece):
    x = None
    y = None
    
    def __init__(self, alliance):
        self.alliance = alliance
    
    def __repr__(self):
        return "B" if self.alliance == "Blacks" else "b"
    
    