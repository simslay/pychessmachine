# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 18:55:17 2019

@author: simslay
"""

from pgame.players.player import Player
from pgame.players.player import Fevals
from pgame.ai.node import Node
from pgame.ai.aitools import AITools
import pgame.ai.horizon1
from pgame.ai.alphabeta import AlphaBeta
import random

class AIWhites(Player):
    feval = Fevals.w_feval
    mode = "Horizon1"
    PMAX = 2
    
    def __init__(self):
        self.alliance = "Whites"
        self.ptype = "Artificial"
        
    def enter_move(self, game, check):
        state = game.state
        node = None
		
        node = Node(state, ((None, None), (None, None)), 0, 0)
		
        if self.mode == "Horizon1":
            nodes = None
            nodes = horizon1.Horizon1.expand_eval(game, check, node)
            
            return AITools.search_optimal_move(nodes)
        elif self.mode == "AlphaBeta":
            return AlphaBeta.alpha_beta_search(game, node, self.feval, self.PMAX)
        return None
    
    # fonction d'evaluation
    @staticmethod
    def feval(game, state, board):
        res = 0.
        rand = random()/10
		
        if AIWhites.feval == Fevals.w_feval:
            weights = [4, 5, 10, 5, 4]
            #weights = [1, 0, 10, 0, 1]
            #weights = [0, 0, 10, 0, 0]

            fevals = [AIWhites.feval_own_captures(state),
                     AIWhites.feval_opponent_captures(state),
                     AIWhites.feval_checkmate(game, state),
                     AIWhites.feval_stalemate(game, state),
                     AIWhites.feval_promotion(state)]
			
            for i in range(len(weights)):
                res += weights[i]*fevals[i];
            return res + rand;
        elif AIWhites.feval == Fevals.w_alea:
            return AIWhites.feval_alea();
        if AIWhites.feval == Fevals.w_captures:
            return AIWhites.feval_own_captures(state) + rand;
        if AIWhites.feval == Fevals.w_checkmate:
            return AIWhites.feval_checkmate(game, state) + rand;
        else:
            return AIWhites.feval_alea()

    # fonction d'evaluation aleatoire
    @staticmethod
    def feval_alea():
        return random()