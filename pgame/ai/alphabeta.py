# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 19:57:54 2019

@author: simslay
"""

import pgame.ai.aitools
import pgame.ai.horizon1

class AlphaBeta():
    @staticmethod
    def alpha_beta_search(game, n, fev, PMAX):
        valueNodes = None
        state = game.state

        valueNodes = AlphaBeta.max_value(game, n, fev, PMAX, -999999, 999999)
        game.state = state
        
        return pgame.ai.aitools.AITools.search_move(valueNodes)
    
    @staticmethod
    def max_value(game, n, fev, PMAX, alpha, beta):
        v = -999999;
        state = n.state
        
        game.state = state
        
        if pgame.ai.aitools.AITools.is_end_of_exploration(game, n, PMAX):
            f = pgame.ai.aitools.AITools.eval(game, fev, game.state, game.state.board)
            nodes = []
            nodes.append(n)
            n.f = f
            
            return (f, nodes)
        
        nodes = pgame.ai.horizon1.Horizon1.expand_eval(game, state.check, n)
        
        for i in range(len(nodes)):
            node = nodes[i]
            
            game.state = node.state
            v = max(v, AlphaBeta.min_value(game, node, fev, PMAX, alpha, beta)[0])
            
            if v >= beta:
                n.f = v
                
                return (v, nodes)
            
            alpha = max(alpha, v)
        
        n.f = v
        
        return (v, nodes)
    
    @staticmethod
    def min_value(game, n, fev, PMAX, alpha, beta):
        v = 999999
        state = n.state
        
        game.state = state
        
        if pgame.ai.aitools.AITools.is_end_of_exploration(game, n, PMAX):
            f = pgame.ai.aitools.AITools.eval(game, fev, game.state, game.state.board)
            nodes = []
            print("n.getDepth " + str(n.depth) + " " + f)
            nodes.append(n)
            n.f = f
            return (f, nodes)
        
        nodes = pgame.ai.horizon1.Horizon1.expand_eval(game, state.check, n)
        for i in range(len(nodes)):
            node = nodes[i]
            
            game.state = node.state
            v = min(v, AlphaBeta.max_value(game, node, fev, PMAX, alpha, beta)[0])
            
            if v <= alpha:
                n.f = v
                
                return (v, nodes)
            beta = min(beta, v)
        
        n.f = v
        
        return (v, nodes)
