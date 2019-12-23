from game.pieces.piece import Piece

class King(Piece):
    x = None
    y = None
    
    def __init__(self, alliance):
        self.alliance = alliance
        self.nom = "kng"
    
    def __repr__(self):
        return "K" if self.alliance == "Blacks" else "k"
    
    def is_valid_move(self, x1, y1, x2, y2, board, player, check):
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
