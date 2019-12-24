# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 17:56:41 2019

@author: simslay
"""

import players.aiwhites
import players.aiblacks
from ai.node import Node
from pgame.gametools import GameTools
from state import State
from players.aiwhites import AIWhites
from players.aiblacks import AIBlacks

class Horizon1():
    @staticmethod
    def successors(game, state, check):
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

                for j in range(len(valid_moves)):
                    move = valid_moves[j]

                    state_copy = State(state)

                    if game.verify_and_play_move(state_copy, move[0][0], move[0][1], move[1][0], move[1][1], True):
                        game.state = state_copy
                        if state_copy.player.alliance == "Whites":
                            if GameTools.black_is_checkmate(game):
                                continue
                        elif state_copy.player.alliance == "Blacks":
                            if GameTools.white_is_checkmate(game):
                                continue

						# promotion
#						for (int k=0; k<16; k++) {
#							if (stateCopy.getWhite()[k]!=null && stateCopy.getWhite()[k].isPromoted())
#								stateCopy.getWhite()[k].setPromoted(false);
#							if (stateCopy.getBlack()[k]!=null && stateCopy.getBlack()[k].isPromoted())
#								stateCopy.getBlack()[k].setPromoted(false);
#						}
                        if (pieces[i].nom == "pwn" and
                            pieces[i].alliance == "Whites" and
                            move[1][1] == 0):

                            for k in range(4):
                                successors.append((state_copy, (move[0], move[1], [k])))
                            continue								
                        elif (pieces[i].nom == "pwn" and
                              pieces[i].alliance == "Blakcs" and
                              move[1][1] == 7):

                            for k in range(4):
                                successors.append((state_copy, (move[0], move[1], [k])))
                            continue						

                        successors.append((state_copy, move))
                game.state = state

        return successors
    
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

        successors = Horizon1.successors(game, state, check)

        if successors != None and len(successors) != 0:
            for i in range(len(successors)):
                new_state = successors[i].state
                game.state = new_state

                if state.player.alliance == "Whites":
                    f = AIWhites.feval(game, new_state, new_state.board)
                elif state.player.alliance == "Blacks":
                    f = AIBlacks.feval(game, new_state, new_state.board)

                move = successors[i].move
                nodes.append(Node(new_state, move, f, n.depth+1))

        game.state = game_state

        return nodes
