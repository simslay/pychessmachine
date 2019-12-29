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
from datetime import datetime
from pgame.gametools import GameTools

class AIBlacks(Player):
    feval_name = Fevals.b_feval
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
        
        random.seed(datetime.now())
        
        if AIBlacks.feval_name.name == 'b_feval':
            weights = [4, 5, 10, 5, 4]
            #weights = {1, 0, 10, 0, 1}
            #weights = {0, 0, 10, 0, 0}

            fevals = [AIBlacks.feval_own_captures(state),
                      AIBlacks.feval_opponent_captures(state),
                      AIBlacks.feval_checkmate(game, state),
                      AIBlacks.feval_stalemate(game, state),
                      AIBlacks.feval_promotion(state)]

            for i in range(len(weights)):
                res += weights[i] * fevals[i]

            return res + random.random()/10
        elif AIBlacks.feval_name.name == 'b_alea':
            return AIBlacks.feval_alea()
        elif AIBlacks.feval_name.name == 'b_captures':
            return AIBlacks.feval_own_captures(state) + + random.random()/10;
        elif AIBlacks.feval_name.name == 'b_checkmate':
            return AIBlacks.feval_checkmate(game, state) + + random.random()/10;
        else:
            return AIBlacks.feval_alea()

    # fonction d'evaluation aleatoire
    @staticmethod
    def feval_alea():
        random.seed(datetime.now())
        
        return random.random()

    # fonction d'evaluation selon valeur de la piece capturee a l'adversaire
    @staticmethod
    def feval_own_captures(state):
        black_captures = state.black_captures
        res = 0.
        
        for i in range(len(black_captures)):
            if black_captures[i].nom == "pwn":
                res += 1
            elif black_captures[i].nom == "knt":
                res += 3
            elif black_captures[i].nom == "bsp":
                res += 3
            elif black_captures[i].nom == "rok":
                res += 5
            elif black_captures[i].nom == "qun":
                res += 9
        
        return res
    
    # fonction d'evaluation selon valeur de la piece capturee par l'adversaire
    @staticmethod
    def feval_opponent_captures(state):
        white_captures = state.white_captures
        res = 0.
        
        for i in range(len(white_captures)):
            if white_captures[i].nom == "pwn":
                res -= 1
            elif white_captures[i].nom == "knt":
                res -= 3
            elif white_captures[i].nom == "bsp":
                res -= 3
            elif white_captures[i].nom == "rok":
                res -= 5
            elif white_captures[i].nom == "qun":
                res -= 9
        
        return res
    
    # fonction d'evaluation du mat
    @staticmethod
    def feval_checkmate(game, state):
        game_state = game.state
        res = 0.
        
        game.state = state
        
        if GameTools.white_is_checkmate(game):
            res = 100
        
        game.state = game_state
        
        return res
    
    # fonction d'evaluation du stalemate
    @staticmethod
    def feval_stalemate(game, state):
        game_state = game.state
        res = 0.
        
        game.state = state
        
        if GameTools.white_is_stalemate(game):
            res = -10
        
        game.state = game_state
        
        return res
    
    # fonction d'evaluation de la promotion
    def feval_promotion(state):
        board = state.board
        piece = None
        
        for i in range(8):
            for j in range(8):
                piece = board[i][j]
                if piece != None and piece.alliance == "Blacks" and piece.promoted:
                    if piece.nom == "knt":
                        return 3
                    elif piece.nom == "bsp":
                        return 3
                    elif piece.nom == "rok":
                        return 5
                    elif piece.nom == "qun":
                        return 9

        return 0