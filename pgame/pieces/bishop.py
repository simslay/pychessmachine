from pgame.pieces.piece import Piece

class Bishop(Piece):
    x = None
    y = None
    
    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            foundOneArg = True
            theOnlyArg = args[0]
        else:
            foundOneArg = False
            theOnlyArg  = None
        
        if foundOneArg and isinstance(theOnlyArg, Piece):
            self.init(theOnlyArg)
        else:
            self.alliance = theOnlyArg
            self.nom = "bsp"
    
    def init(self, p):
        super().init(p)
    
    def __repr__(self):
        return "B" if self.alliance == "Blacks" else "b"
    
    def is_valid_move(self, x1, y1, x2, y2, board, player, check):
        # commun a toutes les pieces (debut)
        if x1 == x2 and y1 == y2:
            return False
        if not (self.alliance == player.alliance and
             ((board[y2][x2] != None and board[y2][x2].alliance != self.alliance) or
              board[y2][x2] == None)):
            return False
        # commun a toutes les pieces (debut)
		
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
