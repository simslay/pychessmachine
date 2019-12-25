# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 20:59:23 2019

@author: simslay
"""

from pgame.pieces.pawn import Pawn
from pgame.pieces.rook import Rook
from pgame.pieces.knight import Knight
from pgame.pieces.bishop import Bishop
from pgame.pieces.queen import Queen
from pgame.pieces.king import King
import pgame.state

class GameTools:
    def __init__(self):
        pass
    
    @staticmethod
    def convert_x(square, p_size, offset):
		return (ord(square[0]) - ord('a')) * p_size + offset
	
    @staticmethod
	def convert_y(square, p_size):
		return abs(int(square[1]) - 8) * p_size + offset
    
    @staticmethod
    def square(px, py):
		x = chr(ord('a')+int(px/80))
        y = 8-int(py/80)
		return str(x) + str(y)
    
    @staticmethod
    def valid_moves(game, piece, check):
        list = None
        square1 = None
        board = game.state.board
        p = None
        player = game.state.player

        list = []
    
        if piece == None:
            return list
        square1 = (piece.x, piece.y)

        if piece.nom == "pwn":
            p = Pawn(piece)
        elif piece.nom == "rok":
            p = Rook(piece)
        elif piece.nom == "knt":
            p = Knight(piece)
        elif piece.nom == "bsp":
            p = Bishop(piece)
        elif piece.nom == "qun":
            p = Queen(piece)
        elif piece.nom == "kng":
            p = King(piece)
		
        if p == None:
            return list
		
		
        for i in range(8):
            for j in range(8):
                if p.is_valid_move(square1[0], square1[1], i, j, board, player, check):
                    list.append((square1, (i, j)));

        return list

    def white_is_check(game, state, x, y):
        board = state.board
        black_pieces = state.black_pieces
        piece = None

        for i in range(16):
            piece = black_pieces[i]

            if piece != None:
                if piece.is_valid_move(piece.x, piece.y, x, y, board, game.blacks_player, False):
                    return True
        return False
    
    def black_is_check(game, state, x, y):
        board = state.board
        white_pieces = state.white_pieces
        piece = None

        for i in range(16):
            piece = white_pieces[i]

            if piece != None:
                if piece.is_valid_move(piece.x, piece.y, x, y, board, game.whites_player, False):
                    return True

        return False
    
    @staticmethod
    def white_is_checkmate(game):
        state = game.state
        state_copy = None
        wKing = state.wking
        x = wKing.x
        y = wKing.y
        white_pieces = state.white_pieces
        valid_moves = []
        move = []

        state_copy = state.State(state)

        if game.state.player.alliance == "Blakcs":
            if GameTools.white_is_check(game, state_copy, x, y):
                print("White will be check!")
                state.player = GameTools.change_player(state.player, game)
                return True
            return False

        state_copy = state.State(state)

        if GameTools.white_is_check(game, state_copy, x, y):

            for i in range(16):
                valid_moves = GameTools.valid_moves(game, white_pieces[i], True)
                if len(valid_moves) == 0:
                    continue

                for j in range(len(valid_moves)):
                    move = valid_moves[j]
                    state_copy = state.State(state)

                    if state_copy == None:
                        return False

                    game.verify_and_play_move(state_copy, move[0][0], move[0][1], move[1][0], move [1][1], True)

                    if not GameTools.white_is_check(game, state_copy, state_copy.wking.x, state_copy.wking.y):
                        print("Check!")
                        state.check = True
                        return False
            print("Checkmate! Black wins")
            return True

        return False

    @staticmethod
    def black_is_checkmate(game):
        state = game.state
        state_copy = None
        bking = state.bking
        x = bking.x
        y = bking.y
        black_pieces = state.black_pieces
        valid_moves = None
        move = None

        state_copy = state.State(state)

        if game.state.player.alliance == "Whites":
            if GameTools.black_is_check(game, state_copy, x, y):
                print("Black will be check!")
                state.player = GameTools.change_player(state.player, game)
                return True
            return False

        state_copy = state.State(state)
		
        if GameTools.black_is_check(game, state_copy, x, y):
            for i in range(16):
                valid_moves = valid_moves(game, black_pieces[i], True)
                if len(valid_moves) == 0:
                    continue

                for j in range(len(valid_moves)):
                    move = valid_moves[j]
                    state_copy = state.State(state)

                    if state_copy == None:
                        return False

                    game.verify_and_play_move(state_copy, move[0][0], move[0][1], move[1][0], move [1][1], True)

                    if not GameTools.black_is_check(game, state_copy, state_copy.bking.x, state_copy.bking.y):
                        print("Check!")
                        state.check = True
                        return False
            print("Checkmate! White wins")
            return True
        return False
