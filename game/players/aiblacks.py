# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 18:55:37 2019

@author: simslay
"""

from game.players.player import Player
from game.players.player import Fevals
from game.ai.node import Node
from game.ai.aitools import AITools
import random

class Blacks(Player):
    feval = Fevals.w_feval
    mode = "Horizon1"
    PMAX = 2
    
    def __init__(self):
        self.alliance = "Blacks"
    
    def enter_move(self, game, check):
        state = game.state
        node = None
		
        node = Node(state, ((None, None), (None, None), 0, 0)
		
		if mode == "Horizon1"
            nodes = None
            nodes = Horizon1.expand_eval(game, check, node)
            return AITools.search_optimal_move(nodes)
        elif mode == "AlphaBeta"
			return AlphaBeta.alpha_beta_search(game, node, self.feval, PMAX)
        return None
