from pieces.knight import Knight

class State():
    def __init__(self):
        self.board = [[Knight("Black"), Knight("Black")]]
        
        self.board[0][0].x = 0
        self.board[0][0].y = 0
        self.board[0][1].x = 1
        self.board[0][1].y = 0