# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 17:56:41 2019

@author: simslay
"""

from game.players.aiwhites import AIWhites
from game.players.aiblacks import AIBlacks

class Horizon1():
    @staticmethod
    def expand_eval(game, check, n):
		state = n.state
        new_state = None
		game_state = game.state
		nodes = None
		successors = None
		move = None
		f = 0.
		
		nodes = []
		
		successors = self.successors(game, state, check)
		
		if successors != None and len(successors) != 0:
			for i in range(len(successors)):
				new_state = successors[i].state
				game.state = new_state

				if state.player.alliance == "Whites":
					f = AIWhites.feval(game, new_state, new_state.board)
				else if state.player.alliance == "Whites":
					f = AIBlack.feval(game, new_state, new_state.board)
			
				move = successors[i].move
				nodes.append(Node(new_state, move, f, n.depth+1))
			}
		}

		game.state = game_state
		
		return nodes
    
    def successors(game, state, check):
        return None