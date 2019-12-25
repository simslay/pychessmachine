from pgame.pieces.piece import Piece

class Knight(Piece):
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
            self.nom = "knt"
    
    def init(self, p):
        super(p)
    
    def __repr__(self):
        return "N" if self.alliance == "Blacks" else "n"
    
    def is_valid_move(self, x1, y1, x2, y2, board, player, check):
        # commun a toutes les pieces (debut)
        if x1 == x2 and y1 == y2:
            return False
        if not (self.alliance == player.alliance and
             ((board[y2][x2] != None and board[y2][x2].alliance != self.alliance) or
              board[y2][x2] == None)):
            return False
        # commun a toutes les pieces (fin)
        
        # verification du mouvement en L
        if ((x2 == x1+1 and y2 == y1+2) or
            (x1 == x2+1 and y2 == y1+2) or
            (x2 == x1+1 and y1 == y2+2) or
            (x1 == x2+1 and y1 == y2+2) or
            (x2 == x1+2 and y2 == y1+1) or
            (x1 == x2+2 and y2 == y1+1) or
            (x2 == x1+2 and y1 == y2+1) or
            (x1 == x2+2 and y1 == y2+1)):
            return True

        return False