from game.pieces.piece import Piece

class King(Piece):
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
            self.nom = "kng"

    def init(self, p):
        super(p)
    
    def __repr__(self):
        return "K" if self.alliance == "Blacks" else "k"
    
    def is_valid_move(self, x1, y1, x2, y2, board, player, check):
        # commun a toutes les pieces (debut)
        if x1 == x2 and y1 == y2:
            return False
        if not (self.alliance == player.alliance and
             ((board[y2][x2] != None and board[y2][x2].alliance != self.alliance) or
              board[y2][x2] == None)):
            return False
        # commun a toutes les pieces (debut)
        
        if ((x1 == x2+1 and y1 == y2+1) or
        (x1 == x2+1 and y1 == y2-1) or
        (x1 == x2+1 and y1 == y2) or
        (x1 == x2-1 and y1 == y2+1) or
        (x1 == x2-1 and y1 == y2-1) or
        (x1 == x2-1 and y1 == y2) or
        (x1 == x2 and y1 == y2+1) or
        (x1 == x2 and y1 == y2-1)):
            self.castling_poss = False
            
            return True	
        elif (self.alliance == "Whites" and not check): # castling
            if self.castling_poss == True:
                if x1 == 4 and y1 == 7 and y2 == 7:
                    if (x2 == 6 and board[7][5] == None and
                    board[7][7] != None and board[7][7].nom == "rok" and
                    board[7][7].castling_poss):
                        self.castling_poss = False
                        
                        return True
                    elif (x2 == 2 and board[7][3] == None and
                    board[7][0] != None and board[7][0].nom == "rok" and
                    board[7][0].castling_poss):
                        self.castling_poss = False

                        return True
        elif self.alliance == "Blacks" and not check: # castling
            if self.castling_poss == True:
                if x1 == 4 and y1 == 0 and y2 == 0:
                    if (x2 == 6 and board[0][5] == None and
                    board[0][7] != None and board[0][7].nom == "rok" and
                    board[0][7].castling_poss):                            
                        self.castling_poss = False
                        
                        return True
                    elif (x2 == 2 and board[0][3] == None and
                    board[0][0] != None and board[0][0].nom == "rok" and
                    board[0][0].castling_poss):
                        self.castling_poss = False
                        return True
        return False
