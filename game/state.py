from game.pieces.bishop import Bishop
from game.pieces.king import King
from game.pieces.knight import Knight
from game.pieces.pawn import Pawn
from game.pieces.queen import Queen
from game.pieces.rook import Rook
from game.pieces.piece import Piece

class State():
    board = []
    white_pieces = None
    black_pieces = None
    white_captures = [] # black pieces
    black_captures = [] # white pieces
    player = None
    move = ""
    white_king = None
    black_king = None
    check = False
    
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
    
    def init(self, state):
        self.bKing = King(state.bking)
		self.wKing = King(state.wking)
		
		black=new Piece[16];
		for (int i=0; i<16; i++)
			if (state.black[i] != null) {
				if (state.black[i].getClass() == new Pawn().getClass())
					black[i] = new Pawn((Pawn) state.black[i]);
				else if (state.black[i].getClass() == new Rook().getClass())
					black[i] = new Rook((Rook) state.black[i]);
				else if (state.black[i].getClass() == new Knight().getClass())
					black[i] = new Knight((Knight) state.black[i]);
				else if (state.black[i].getClass() == new Bishop().getClass())
					black[i] = new Bishop((Bishop) state.black[i]);
				else if (state.black[i].getClass() == new Queen().getClass())
					black[i] = new Queen((Queen) state.black[i]);
				else if (state.black[i].getClass() == new King().getClass())
					black[i] = bKing;
			} else
				black[i] = null;
		
		white=new Piece[16];
		for (int i=0; i<16; i++)
			if (state.white[i] != null) {
				if (state.white[i].getClass() == new Pawn().getClass())
					white[i] = new Pawn((Pawn) state.white[i]);
				else if (state.white[i].getClass() == new Rook().getClass())
					white[i] = new Rook((Rook) state.white[i]);
				else if (state.white[i].getClass() == new Knight().getClass())
					white[i] = new Knight((Knight) state.white[i]);
				else if (state.white[i].getClass() == new Bishop().getClass())
					white[i] = new Bishop((Bishop) state.white[i]);
				else if (state.white[i].getClass() == new Queen().getClass())
					white[i] = new Queen((Queen) state.white[i]);
				else if (state.white[i].getClass() == new King().getClass())
					white[i] = wKing;
			} else
				white[i] = null;
		
		board=new Piece[8][8];
		for (int i=0; i<8; i++)
			for (int j=0; j<8; j++) {
				if (state.board[i][j] != null) {
					for (int k=0; k<16; k++)
						if (state.board[i][j] == state.black[k]) {
							board[i][j] = black[k];
							break;
						} else if (state.board[i][j] == state.white[k]) {
							board[i][j] = white[k];
							break;
						}
				} else
					board[i][j] = null;
			}

		if (state.getPlayer().getColor() == Game.WHITE &&
			state.getPlayer().getType() == Game.HUMAN)
			player = new HumanWhite();
		if (state.getPlayer().getColor() == Game.BLACK &&
			state.getPlayer().getType() == Game.HUMAN)
			player = new HumanBlack();
		if (state.getPlayer().getColor() == Game.WHITE &&
			state.getPlayer().getType() == Game.ARTIFICIAL)
			player = new ArtificialWhite();
		if (state.getPlayer().getColor() == Game.BLACK &&
			state.getPlayer().getType() == Game.ARTIFICIAL)
			player = new ArtificialBlack();
		
		whiteCaptures=new Vector<Piece>();
		for (int i=0; i<state.getWhiteCaptures().size(); i++) {
			if (state.getWhiteCaptures().get(i).getClass() == new Pawn().getClass())
				whiteCaptures.add(new Pawn((Pawn) state.getWhiteCaptures().get(i)));
			else if (state.getWhiteCaptures().get(i).getClass() == new Rook().getClass())
				whiteCaptures.add(new Rook((Rook) state.getWhiteCaptures().get(i)));
			else if (state.getWhiteCaptures().get(i).getClass() == new Knight().getClass())
				whiteCaptures.add(new Knight((Knight) state.getWhiteCaptures().get(i)));
			else if (state.getWhiteCaptures().get(i).getClass() == new Bishop().getClass())
				whiteCaptures.add(new Bishop((Bishop) state.getWhiteCaptures().get(i)));
			else if (state.getWhiteCaptures().get(i).getClass() == new Queen().getClass())
				whiteCaptures.add(new Queen((Queen) state.getWhiteCaptures().get(i)));
			else if (state.getWhiteCaptures().get(i).getClass() == new King().getClass())
				whiteCaptures.add(new King((King) state.getWhiteCaptures().get(i)));
			else
				throw new UndefinedPieceException();
		}
		
		blackCaptures=new Vector<Piece>();
		for (int i=0; i<state.getBlackCaptures().size(); i++) {
			if (state.getBlackCaptures().get(i).getClass() == new Pawn().getClass())
				blackCaptures.add(new Pawn((Pawn) state.getBlackCaptures().get(i)));
			else if (state.getBlackCaptures().get(i).getClass() == new Rook().getClass())
				blackCaptures.add(new Rook((Rook) state.getBlackCaptures().get(i)));
			else if (state.getBlackCaptures().get(i).getClass() == new Knight().getClass())
				blackCaptures.add(new Knight((Knight) state.getBlackCaptures().get(i)));
			else if (state.getBlackCaptures().get(i).getClass() == new Bishop().getClass())
				blackCaptures.add(new Bishop((Bishop) state.getBlackCaptures().get(i)));
			else if (state.getBlackCaptures().get(i).getClass() == new Queen().getClass())
				blackCaptures.add(new Queen((Queen) state.getBlackCaptures().get(i)));
			else if (state.getBlackCaptures().get(i).getClass() == new King().getClass())
				blackCaptures.add(new King((King) state.getBlackCaptures().get(i)));
			else
				throw new UndefinedPieceException();
		}
		
		move = state.move.clone();
		
		review = new Vector<String[]>();
		
		for (int i=0; i<state.review.size(); i++)
			review.add(state.review.get(i).clone());
		
		check = state.check;
    
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
