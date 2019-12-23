from game.pieces.piece import Piece

class Pawn(Piece):
    x = None
    y = None
    
    def __init__(self, alliance):
        self.alliance = alliance
        self.nom = "pwn"
    
    def __repr__(self):
        return "P" if self.alliance == "Blacks" else "p"
    
    def is_valid_move(self, x1, y1, x2, y2, board, player, check):
        # commun a toutes les pieces (debut)
        if x1 == x2 and y1 == y2:
            return False
        if not (self.alliance == player.alliance and
             ((board[y2][x2] != None and board[y2][x2].alliance != self.alliance) or
              board[y2][x2] == None)):
            return False
        # commun a toutes les pieces (fin)
        
        if self.alliance == "Whites":
            if x1 == x2 and (y2-y1 == -1 or y2-y1 == -2):
                if board[y2][x2] != None:
                    return False
                # premier coup du pion de deux cases en avant
                if y1 == 6 and y2-y1 == -2:
                    if board[y1-1][x1] == None:
                        en_passant_risk = True
                        
                        return True
                    else:
                        return False
                if y1 != 6 and y2-y1 == -2:
                    return False
                return True

            # mouvement en diagonale
            if ((x2 == x1+1 or x2 == x1-1) and y2 == y1-1 and
                ((board[y2][x2] != None and board[y2][x2].alliance == "Blacks") or
                 (y1 == 3 and board[y1][x2]!=null and board[y1][x2].nom == "pwn" and
                  board[y1][x2].en_passant_risk) ) ):
                return True
			
            return False		
        if self.alliance == "Blacks":
            if x1 == x2 and (y2-y1 == 1 or y2-y1 == 2):
                if board[y2][x2] != None:
                    return False
                # premier coup du pion de deux cases en avant
                if y1 == 1 and y2-y1 == 2:
                    if board[y1+1][x1] == None:
                        en_passant_risk = True
                        return True
                    else:
                        return False
                if y1 != 1 and y2-y1 == 2:
                    return False
                return True

            if ((x2 == x1+1 or x2 == x1-1) and y2 == y1+1 and
                ((board[y2][x2] != None and board[y2][x2].alliance == "Whites") or
                 (y1 == 4 and board[y1][x2] != None and board[y1][x2].nom.equals("pwn") and
                  board[y1][x2].en_passant_risk) ) ):
                return True

            return False

        return False