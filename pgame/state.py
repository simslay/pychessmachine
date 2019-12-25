from pgame.pieces.bishop import Bishop
from pgame.pieces.king import King
from pgame.pieces.knight import Knight
from pgame.pieces.pawn import Pawn
from pgame.pieces.queen import Queen
from pgame.pieces.rook import Rook
from pgame.players.whites import Whites
from pgame.players.blacks import Blacks
from pgame.players.aiwhites import AIWhites
from pgame.players.aiblacks import AIBlacks

class State():
    board = []
    white_pieces = None
    black_pieces = None
    white_captures = [] # black pieces
    black_captures = [] # white pieces
    player = None
    move = ""
    wking = None
    bking = None
    check = False
    review = None
    
    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            foundOneArg = True
            theOnlyArg = args[0]
        else:
            foundOneArg = False
            theOnlyArg  = None

        if foundOneArg and isinstance(theOnlyArg, State):      
            self.init(theOnlyArg)
        else:
            self.board = [[Rook("Blacks"), Knight("Blacks"), Bishop("Blacks"), Queen("Blacks"), King("Blacks"), Bishop("Blacks"), Knight("Blacks"), Rook("Blacks")],
                          [Pawn("Blacks"), Pawn("Blacks"), Pawn("Blacks"), Pawn("Blacks"), Pawn("Blacks"), Pawn("Blacks"), Pawn("Blacks"), Pawn("Blacks")],
                          [None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None],
                          [Pawn("Whites"), Pawn("Whites"), Pawn("Whites"), Pawn("Whites"), Pawn("Whites"), Pawn("Whites"), Pawn("Whites"), Pawn("Whites")],
                          [Rook("Whites"), Knight("Whites"), Bishop("Whites"), Queen("Whites"), King("Whites"), Bishop("Whites"), Knight("Whites"), Rook("Whites")]]
            
            self.white_pieces = [self.board[7][0], self.board[7][1], self.board[7][2], self.board[7][3],
                             self.board[7][4], self.board[7][5], self.board[7][6], self.board[7][7],
                             self.board[6][0], self.board[6][1], self.board[6][2], self.board[6][3],
                             self.board[6][4], self.board[6][5], self.board[6][6], self.board[6][7]]
            
            self.black_pieces = [self.board[0][0], self.board[0][1], self.board[0][2], self.board[0][3],
                             self.board[0][4], self.board[0][5], self.board[0][6], self.board[0][7],
                             self.board[1][0], self.board[1][1], self.board[1][2], self.board[1][3],
                             self.board[1][4], self.board[1][5], self.board[1][6], self.board[1][7]]
            
            for x in range(8):
                for y in range(8):
                    if self.board[x][y] != None:
                        self.board[x][y].x = x
                        self.board[x][y].y = y
    
    # constructeur par recopie
    def init(self, state):
        self.bking = King(state.bking)
        self.wking = King(state.wking)

        self.black_pieces = []
        for i in range(16):
            if state.black_pieces[i] != None:
                if isinstance(state.black_pieces[i], Pawn):
                    self.black_pieces[i] = Pawn(state.black_pieces[i])
                elif isinstance(state.black_pieces[i], Rook):
                    self.black_pieces[i] = Rook(state.black_pieces[i])
                elif isinstance(state.black_pieces[i], Knight):
                    self.black_pieces[i] = Knight(state.black_pieces[i])
                elif isinstance(state.black_pieces[i], Bishop):
                    self.black_pieces[i] = Bishop(state.black[i])
                elif isinstance(state.black_pieces[i], Queen):
                    self.black_pieces[i] = Queen(state.black[i])
                elif isinstance(state.black_pieces[i], King):
                    self.black_pieces[i] = self.bking;
            else:
                self.black_piececs[i] = None

        self.white_pieces = []
        for i in range(16):
            if state.white[i] != None:
                if isinstance(state.white_pieces[i], Pawn):
                    self.white_pieces[i] = Pawn(state.white_pieces[i])
                elif isinstance(state.white_pieces[i], Rook):
                    self.white_pieces[i] = Rook(state.white_pieces[i])
                elif isinstance(state.white_pieces[i], Knight):
                    self.white_pieces[i] = Knight(state.white_pieces[i])
                elif isinstance(state.white_pieces[i], Bishop):
                    self.white_pieces[i] = Bishop(state.white_pieces[i])
                elif isinstance(state.white_pieces[i], Queen):
                    self.white_pieces[i] = Queen(state.white_pieces[i])
                elif isinstance(state.white_pieces[i], King):
                    self.white_pieces[i] = self.wking;
            else:
                self.white_pieces[i] = None
		
        self.board = []
        for i in range(8):
            for j in range(8):
                if state.board[i][j] != None:
                    for k in range(16):
                        if state.board[i][j] == state.black_pieces[k]:
                            self.board[i][j] = self.black_pieces[k]
                            break
                        elif state.board[i][j] == state.white_pieces[k]:
                            self.board[i][j] = self.white_pieces[k]
                            break
                else:
                    self.board[i][j] = None

        if (state.player.alliance == "Whites" and
            state.player.ptype == "Human"):
            self.player = Whites()
        if (state.player.alliance == "Blacks" and
            state.player.ptype == "Human"):
            self.player = Blacks()
        if (state.player.alliance == "Whites" and
            state.player.ptype == "Artificial"):
            self.player = AIWhites()
        if (state.player.alliance == "Blacks" and
            state.player.ptype == "Artificial"):
            self.player = AIBlacks()
		
        self.white_captures = []
        for i in range(len(state.white_captures)):
            if isinstance(state.white_captures[i], Pawn):
                self.white_captures.append(Pawn(state.white_captures[i]))
            elif isinstance(state.white_captures[i], Rook):
                self.white_captures.append(Rook(state.whites_captures[i]))
            elif isinstance(state.white_captures[i], Knight):
                self.white_captures.append(Knight(state.whites_captures[i]))
            elif isinstance(state.white_captures[i], Bishop):
                self.white_captures.append(Bishop(state.whites_captures[i]))
            elif isinstance(state.white_captures[i], Queen):
                self.white_captures.append(Queen(state.whites_captures[i]))
            elif isinstance(state.white_captures[i], King):
                self.white_captures.append(King(state.whites_captures[i]))

        self.black_captures = []
        for i in range(len(state.black_captures)):
            if isinstance(state.black_captures[i], Pawn):
                self.black_captures.append(Pawn(state.black_captures[i]))
            elif isinstance(state.black_captures[i], Rook):
                self.black_captures.append(Rook(state.black_captures[i]))
            elif isinstance(state.black_captures[i], Knight):
                self.black_captures.append(Knight(state.black_captures[i]))
            elif isinstance(state.black_captures[i], Bishop):
                self.black_captures.append(Bishop(state.black_captures[i]))
            elif isinstance(state.black_captures[i], Queen):
                self.black_captures.append(Queen(state.black_captures[i]))
            elif isinstance(state.black_captures[i], King):
                self.black_captures.append(King(state.black_captures[i]))
		
        self.move = state.move

        review = []

        for i in range(len(state.review)):
            review.append(state.review[i])

        self.check = state.check
    
    def printBoard(self):
        count = 0
        for x in range(8):
            for y in range(8):
                if self.board[x][y] != None:
                    print('|', end=str(self.board[x][y]))
                else:
                    print('|', end='-')
                count += 1
                if count == 8:
                    print('|', end='\n')
                    count = 0
    
    def add_capture(self, piece):
        if piece.alliance == "Whites":
            self.black_captures.append(piece)
        elif piece.alliance == "Blacks":
            self.white_captures.append(piece)
