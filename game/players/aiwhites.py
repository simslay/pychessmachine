# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 18:55:17 2019

@author: simslay
"""

from game.players.player import Player
from game.players.player import Fevals
from game.ai.node import Node
from game.ai.aitools import AITools
import random

class Whites(Player):
    feval = Fevals.w_feval
    mode = "Horizon1"
    PMAX = 2
    
    def __init__(self):
        self.alliance = "Whites"
        
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
    
    # fonction d'evaluation
    @staticmethod
	def feval(game, state, board) {
		res = 0.
		rand = random()/10
		
		if 
		case wFeval :
			double[] weights = {4, 5, 10, 5, 4};
			//double[] weights = {1, 0, 10, 0, 1};
			//double[] weights = {0, 0, 10, 0, 0};
			
			double[] fevals = {	fevalOwnCaptures(state),
								fevalOpponentCaptures(state),
								fevalCheckmate(game, state),
								fevalStalemate(game, state),
								fevalPromotion(state)};
			
			for (int i=0; i<weights.length; i++)
				res += weights[i]*fevals[i];
			//System.out.println("feval: res = "+res);
			return res + rand;
		case wAlea :
			return fevalAlea();
		case wCaptures :
			return fevalOwnCaptures(state) + rand;
		case wCheckmate :
			return fevalCheckmate(game, state) + rand;
		default :
			return fevalAlea()
	}