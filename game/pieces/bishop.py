from game.pieces.piece import Piece

class Bishop(Piece):
    x = None
    y = None
    
    def __init__(self, alliance):
        self.alliance = alliance
        self.nom = "bsp"
    
    def __repr__(self):
        return "B" if self.alliance == "Blacks" else "b"
    
    def is_valid_move(self, x1, y1, x2, y2, board, player, check):
        super(x1, y1, x2, y2, board, player, check)
		
        # verification du mouvement en diagonale
        if x1 == x2 or y1 == y2 or abs(x2-x1) != abs(y2-y1):
            return False
        # verification des cases entre les positions de depart
        # et d'arrivee de la piece
        if x1 < x2 and y1 < y2:
            for i in range(x1+1, x2):
                if board[y1+(i-x1)][i] != None:
                    return False
        if x1 < x2 and y1 > y2:
            for i in range(x1+1, x2):
                if board[y1-(i-x1)][i] != None:
                    return False
        if x1 > x2 and y1 < y2:
            for i in range(x2+1, x1):
                if board[y2-(i-x2)][i] != None:
                    return False
        if x1 > x2 and y1 > y2:
            for i in range(x2+1, x1):
                if board[y2+(i-x2)][i] != None:
                    return False
		
        return True