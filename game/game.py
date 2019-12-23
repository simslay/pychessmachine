# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 21:09:10 2019

@author: simslay
"""

from game.state import State
from game.players.whites import Whites
from game.players.blacks import Blacks

class Game():
    state = None
    whites = None
    blacks = None
    
    def __init__(self):
        self.state = State()
        self.whites = Whites()
        self.blacks = Blacks()
        
        self.state.player = Whites()
        
    def verify_and_play_move(state, x1, y1, x2, y2):
        board = state.board
        whites = state.white_pieces
        blacks = state.black_pieces
        current_player = state.player
        
        piece = board[y1][x1]
        
        if piece != None and (piece.is_valid_move(x1, y1, x2, y2, board, current_player, state.checked) or
			(state.player.type == "Artificial" and piece.promoted)):
            # enlevement de la piece
            board[y1][x1] = None
            