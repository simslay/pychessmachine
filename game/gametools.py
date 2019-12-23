# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 20:59:23 2019

@author: simslay
"""

from game.pieces.pawn import Pawn
from game.pieces.rook import Rook
from game.pieces.knight import Knight
from game.pieces.bishop import Bishop
from game.pieces.queen import Queen
from game.pieces.king import King

class GameTools:
    def __init__(self):
        pass
    
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
