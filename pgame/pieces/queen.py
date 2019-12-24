from pieces.piece import Piece
from pieces.bishop import Bishop
from pieces.rook import Rook

class Queen(Piece):
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
            self.nom = "qun"
    
    def init(self, p):
        super(p)
    
    def __repr__(self):
        return "Q" if self.alliance == "Blacks" else "q"
    
    def is_valid_move(self, x1, y1, x2, y2, board, player, check):
        # commun a toutes les pieces (debut)
        if x1 == x2 and y1 == y2:
            return False
        if not (self.alliance == player.alliance and
             ((board[y2][x2] != None and board[y2][x2].alliance != self.alliance) or
              board[y2][x2] == None)):
            return False
        # commun a toutes les pieces (fin)

        bsp = Bishop(self.alliance)
        bsp.x(self.x)
        bsp.y(self.y)
        rk = Rook(self.alliance)
        rk.x(self.x)
        rk.y(self.y)

        return (bsp.is_valid_move(x1, y1, x2, y2, board, player, check) or
            rk.is_valid_move(x1, y1, x2, y2, board, player, check))