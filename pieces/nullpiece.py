from pieces.piece import Piece

class NullPiece(Piece):
    def __init__(self):
        pass
    
    def __repr__(self):
        return "-"