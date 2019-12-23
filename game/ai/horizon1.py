# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 17:56:41 2019

@author: simslay
"""

import game.players.aiwhites
import game.players.aiblacks
from game.ai.node import Node
from game.gametools import GameTools

class Horizon1():
    @staticmethod
    def successors(_game, state, check):
        state_copy = None
		pieces = []
		successors = []
		valid_moves = []
		move = None
		#JLabel label = new JLabel();
		
		if state.player.alliance == "Whites":
			pieces = state.white_pieces
		elif state.player.alliance == "Blacks":
			pieces = state.black_pieces
		
		successors = []
		
		for i in range(16):
            if pieces[i] != None:
                valid_moves = GameTools.valid_moves(game, pieces[i], check)
				
				for j in range(len(valid_moves))
					move = valid_moves[j]
					
					state_copy = State(state)
					
					if (game.verifyAndPlayMove(stateCopy, move[0][0], move[0][1], move[1][0], move[1][1], true)) {
						//System.out.println("successors");
						game.setState(stateCopy);
						switch (stateCopy.getPlayer().getColor()) {
							case Player.WHITE :
								if (GameUtil.blackIsCheckmate(game, label)) {
									//System.out.println("continue");
									continue;
								}
								break;
							case Player.BLACK :
								if (GameUtil.whiteIsCheckmate(game, label)) {
									//System.out.println("continue");
									continue;
								}
								break;
							default :
								throw new UndefinedPlayerException();
						}
						
						/** promotion **/
						/*for (int k=0; k<16; k++) {
							if (stateCopy.getWhite()[k]!=null && stateCopy.getWhite()[k].isPromoted())
								stateCopy.getWhite()[k].setPromoted(false);
							if (stateCopy.getBlack()[k]!=null && stateCopy.getBlack()[k].isPromoted())
								stateCopy.getBlack()[k].setPromoted(false);
						}*/
						if (pieces[i].getNom().equals("pwn") &&
								pieces[i].getColor() == Game.WHITE &&
								move[1][1] == 0) {
							
							for (int k=0; k<4; k++)
								successors.add(new Pair(stateCopy,
														new int[][]{move[0], move[1], {k}}));
							continue;
								
						} else if (pieces[i].getNom().equals("pwn") &&
								pieces[i].getColor() == Game.BLACK &&
									move[1][1] == 7) {
							
							for (int k=0; k<4; k++)
								successors.add(new Pair(stateCopy,
														new int[][]{move[0], move[1], {k}}));
							continue;
								
						}
						
					
						successors.add(new Pair(stateCopy, move));
					}
				}
				game.setState(state);
			}
		}
		
		return successors
    
    @staticmethod
    def expand_eval(_game, check, n):
        state = n.state
        new_state = None
        game_state = _game.state
        nodes = None
        successors = None
        move = None
        f = 0.

        nodes = []

        successors = Horizon1.successors(_game, state, check)

        if successors != None and len(successors) != 0:
            for i in range(len(successors)):
                new_state = successors[i].state
                _game.state = new_state

                if state.player.alliance == "Whites":
                    f = aiwhites.AIWhites.feval(_game, new_state, new_state.board)
                elif state.player.alliance == "Blacks":
                    f = aiblacks.AIBlacks.feval(_game, new_state, new_state.board)

                move = successors[i].move
                nodes.append(Node(new_state, move, f, n.depth+1))

        _game.state = game_state

        return nodes
