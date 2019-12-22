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
        current_player = state.player
        