# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 18:35:55 2019

@author: simslay
"""

from pgame.gametools import GameTools
import pgame.players.aiwhites
import pgame.players.aiblacks

class AITools():
    @staticmethod
    def search_optimal_move(nodes):
        node = None
        f = 0.
        move = None
        
        if len(nodes) > 0:
            move = nodes[0].action
        else:
            return None

        for i in range(len(nodes)):
            node = nodes[i]

            if node.f > f:
                f = node.f
                move = node.action

        return move
    
    @staticmethod
    def search_move(valueNodes):
        v = valueNodes[0]
        nodes = valueNodes[1]
        
        for i in range(len(nodes)):
            if nodes[i].f == v:
                print("search_move(): " + str(v))
                
                return nodes[i].action

        return None
    
    @staticmethod
    def is_end_of_exploration(game, node, PMAX):
        return node.depth == PMAX or GameTools.is_end_of_game(game)

    @staticmethod
    def eval(game, fev, state, board):
        if fev.name[0] == 'w':
            pgame.players.aiwhites.AIWhites.feval_name = fev
            
            return pgame.players.aiwhites.AIWhites.feval(game, state, board)
        elif fev.name[0] == 'b':
            pgame.players.aiblacks.AIBlacks.feval_name = fev
            
            return pgame.players.aiblacks.AIBlacks.feval(game, state, board)
