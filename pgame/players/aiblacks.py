# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 18:55:37 2019

@author: simslay
"""

from pgame.players.player import Player
from pgame.players.player import Fevals
from pgame.ai.node import Node
from pgame.ai.aitools import AITools
import pgame.ai.horizon1
from pgame.ai.alphabeta import AlphaBeta
import random

class AIBlacks(Player):
    feval = Fevals.w_feval
    mode = "Horizon1"
    PMAX = 2
    
    def __init__(self):
        self.alliance = "Blacks"
        self.ptype = "Artificial"
    
    def enter_move(self, game, check):
        state = game.state
        node = None
		
        node = Node(state, ((None, None), (None, None)), 0, 0)
		
        if self.mode == "Horizon1":
            nodes = None
            nodes = horizon1.Horizon1.expand_eval(game, check, node)
            
            return AITools.search_optimal_move(nodes) # node.action ((x1, y1), (x2, y2))
        elif self.mode == "AlphaBeta":
            return AlphaBeta.alpha_beta_search(game, node, self.feval, self.PMAX)
        return None
