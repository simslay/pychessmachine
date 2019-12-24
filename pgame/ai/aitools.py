# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 18:35:55 2019

@author: simslay
"""

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