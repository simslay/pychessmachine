from pieces.piece import Piece

class Knight(Piece):
    color = None
    x = None
    y = None
    
    def __init__(self, color):
        self.color = color
    
    def __repr__(self):
        return "N" if self.color == "Black" else "n"