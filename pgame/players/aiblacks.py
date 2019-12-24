# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 18:55:37 2019

@author: simslay
"""

from players.player import Player
from players.player import Fevals
from ai.node import Node
from ai.aitools import AITools
import ai.horizon1
from ai.alphabeta import AlphaBeta
import random

class AIBlacks(Player):
    feval = Fevals.w_feval
    mode = "Horizon1"
    PMAX = 2
    
    def __init__(self):
        self.alliance = "Blacks"
    
    def enter_move(self, game, check):
        state = game.state
        node = None
		
        node = Node(state, ((None, None), (None, None)), 0, 0)
		
        if self.mode == "Horizon1":
            nodes = None
            nodes = Horizon1.expand_eval(game, check, node)
            
            return AITools.search_optimal_move(nodes)
        elif self.mode == "AlphaBeta":
            return AlphaBeta.alpha_beta_search(game, node, self.feval, self.PMAX)
        return None
