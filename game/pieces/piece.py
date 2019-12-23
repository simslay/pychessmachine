from abc import abstractmethod

class Piece(object):
    alliance = None
    promoted = False
    castling_poss = True
    nom = None
    en_passant_risk = False
    
    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            foundOneArg = True
            theOnlyArg = args[0]
        else:
            foundOneArg = False
            theOnlyArg  = None
        
        if foundOneArg and isinstance(theOnlyArg, Piece):
            self.init(theOnlyArg)
    
    def init(self, p):
        super()
        
        self.x = p.x
        self.y = p.y
        self.alliance = p.alliance
        self.nom = p.nom
		
        self.en_passant_risk = p.en_passant_risk
        self.castling_poss = p.castling_poss
        self.promoted = p.promoted
    
    @abstractmethod
    def is_valid_move(self, x1, y1, x2, y2, board, player, check):
        pass
