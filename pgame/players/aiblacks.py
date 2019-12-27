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
    feval_name = Fevals.b_alea
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
            nodes = pgame.ai.horizon1.Horizon1.expand_eval(game, check, node)
            
            return AITools.search_optimal_move(nodes) # node.action ((x1, y1), (x2, y2))
        elif self.mode == "AlphaBeta":
            return AlphaBeta.alpha_beta_search(game, node, self.feval, self.PMAX)
        return None

    # fonction d'evaluation
    @staticmethod
    def feval(game, state, board):
        res = 0.
        rand = random.random()/10
        
        if AIBlacks.feval_name.name == 'b_feval':
            weights = [4, 5, 10, 5, 4]
            #weights = {1, 0, 10, 0, 1}
            #weights = {0, 0, 10, 0, 0}

#            fevals = [fevalOwnCaptures(state),
#                                fevalOpponentCaptures(state),
#                                fevalCheckmate(game, state),
#                                fevalStalemate(game, state),
#                                fevalPromotion(state)]
#
#            for i in range(len(weights)):
#                res += weights[i] * fevals[i]

            return res + rand;
        elif AIBlacks.feval_name.name == 'b_alea':
            return AIBlacks.feval_alea()
#        case bCaptures :
#            return fevalOwnCaptures(state) + rand
#        case bCheckmate :
#            return fevalCheckmate(game, state) + rand
#        default :
#            return fevalAlea()

    # fonction d'evaluation aleatoire
    @staticmethod
    def feval_alea():
        return random.random()
