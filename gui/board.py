# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 11:17:33 2019

@author: simslay
"""

import sys
import pygame
from gui.draggablepiece import DraggablePiece
from game.game import Game

piece_width = 80
piece_height = 80

class Board():
    game = None
    
    def __init__(self):
        self.game = Game()
        
    @staticmethod
    def convert_x_y(x, y):
        return x*piece_width, y*piece_height
    @staticmethod
    def get_draggable_pieces(screen):
        draggable_pieces = {}
        
        # rooks
        draggable_wrook1 = DraggablePiece(screen, "./images/200px-Chess_rlt45.svg.png", Board.convert_x_y(0, 7), piece_width, piece_height)
        draggable_pieces["wrook1"] = draggable_wrook1
        draggable_wrook2 = DraggablePiece(screen, "./images/200px-Chess_rlt45.svg.png", Board.convert_x_y(7, 7), piece_width, piece_height)
        draggable_pieces["wrook2"] = draggable_wrook2
        draggable_brook1 = DraggablePiece(screen, "./images/200px-Chess_rdt45.svg.png", Board.convert_x_y(0, 0), piece_width, piece_height)
        draggable_pieces["brook1"] = draggable_brook1
        draggable_brook2 = DraggablePiece(screen, "./images/200px-Chess_rdt45.svg.png", Board.convert_x_y(7, 0), piece_width, piece_height)
        draggable_pieces["brook2"] = draggable_brook2
        
        # bishops
        draggable_wbishop1 = DraggablePiece(screen, "./images/200px-Chess_blt45.svg.png", Board.convert_x_y(2, 7), piece_width, piece_height)
        draggable_pieces["wbishop1"] = draggable_wbishop1
        draggable_wbishop2 = DraggablePiece(screen, "./images/200px-Chess_blt45.svg.png", Board.convert_x_y(5, 7), piece_width, piece_height)
        draggable_pieces["wbishop2"] = draggable_wbishop2
        draggable_bbishop1 = DraggablePiece(screen, "./images/200px-Chess_bdt45.svg.png", Board.convert_x_y(2, 0), piece_width, piece_height)
        draggable_pieces["bbishop1"] = draggable_bbishop1
        draggable_bbishop2 = DraggablePiece(screen, "./images/200px-Chess_bdt45.svg.png", Board.convert_x_y(5, 0), piece_width, piece_height)
        draggable_pieces["bbishop2"] = draggable_bbishop2
        
        # knights
        draggable_wknigth1 = DraggablePiece(screen, "./images/200px-Chess_nlt45.svg.png", Board.convert_x_y(1, 7), piece_width, piece_height)
        draggable_pieces["wknigth1"] = draggable_wknigth1
        draggable_wknigth2 = DraggablePiece(screen, "./images/200px-Chess_nlt45.svg.png", Board.convert_x_y(6, 7), piece_width, piece_height)
        draggable_pieces["wknigth2"] = draggable_wknigth2
        draggable_bknigth1 = DraggablePiece(screen, "./images/200px-Chess_ndt45.svg.png", Board.convert_x_y(1, 0), piece_width, piece_height)
        draggable_pieces["bknigth1"] = draggable_bknigth1
        draggable_bknigth2 = DraggablePiece(screen, "./images/200px-Chess_ndt45.svg.png", Board.convert_x_y(6, 0), piece_width, piece_height)
        draggable_pieces["bknigth2"] = draggable_bknigth2
        
        # queens
        draggable_wqueen = DraggablePiece(screen, "./images/200px-Chess_qlt45.svg.png", Board.convert_x_y(3, 7), piece_width, piece_height)
        draggable_pieces["wqueen"] = draggable_wqueen
        draggable_bqueen = DraggablePiece(screen, "./images/200px-Chess_qdt45.svg.png", Board.convert_x_y(3, 0), piece_width, piece_height)
        draggable_pieces["bqueen"] = draggable_bqueen
        
        # kings
        draggable_wking = DraggablePiece(screen, "./images/200px-Chess_klt45.svg.png", Board.convert_x_y(4, 7), piece_width, piece_height)
        draggable_pieces["wking"] = draggable_wking
        draggable_bking = DraggablePiece(screen, "./images/200px-Chess_kdt45.svg.png", Board.convert_x_y(4, 0), piece_width, piece_height)
        draggable_pieces["bking"] = draggable_bking
        
        # pawns
        draggable_wpawn1 = DraggablePiece(screen, "./images/200px-Chess_plt45.svg.png", Board.convert_x_y(0, 6), piece_width, piece_height)
        draggable_pieces["wpawn1"] = draggable_wpawn1
        draggable_wpawn2 = DraggablePiece(screen, "./images/200px-Chess_plt45.svg.png", Board.convert_x_y(1, 6), piece_width, piece_height)
        draggable_pieces["wpawn2"] = draggable_wpawn2
        draggable_wpawn3 = DraggablePiece(screen, "./images/200px-Chess_plt45.svg.png", Board.convert_x_y(2, 6), piece_width, piece_height)
        draggable_pieces["wpawn3"] = draggable_wpawn3
        draggable_wpawn4 = DraggablePiece(screen, "./images/200px-Chess_plt45.svg.png", Board.convert_x_y(3, 6), piece_width, piece_height)
        draggable_pieces["wpawn4"] = draggable_wpawn4
        draggable_wpawn5 = DraggablePiece(screen, "./images/200px-Chess_plt45.svg.png", Board.convert_x_y(4, 6), piece_width, piece_height)
        draggable_pieces["wpawn5"] = draggable_wpawn5
        draggable_wpawn6 = DraggablePiece(screen, "./images/200px-Chess_plt45.svg.png", Board.convert_x_y(5, 6), piece_width, piece_height)
        draggable_pieces["wpawn6"] = draggable_wpawn6
        draggable_wpawn7 = DraggablePiece(screen, "./images/200px-Chess_plt45.svg.png", Board.convert_x_y(6, 6), piece_width, piece_height)
        draggable_pieces["wpawn7"] = draggable_wpawn7
        draggable_wpawn8 = DraggablePiece(screen, "./images/200px-Chess_plt45.svg.png", Board.convert_x_y(7, 6), piece_width, piece_height)
        draggable_pieces["wpawn8"] = draggable_wpawn8
        
        draggable_bpawn1 = DraggablePiece(screen, "./images/200px-Chess_pdt45.svg.png", Board.convert_x_y(0, 1), piece_width, piece_height)
        draggable_pieces["bpawn1"] = draggable_bpawn1
        draggable_bpawn2 = DraggablePiece(screen, "./images/200px-Chess_pdt45.svg.png", Board.convert_x_y(1, 1), piece_width, piece_height)
        draggable_pieces["bpawn2"] = draggable_bpawn2
        draggable_bpawn3 = DraggablePiece(screen, "./images/200px-Chess_pdt45.svg.png", Board.convert_x_y(2, 1), piece_width, piece_height)
        draggable_pieces["bpawn3"] = draggable_bpawn3
        draggable_bpawn4 = DraggablePiece(screen, "./images/200px-Chess_pdt45.svg.png", Board.convert_x_y(3, 1), piece_width, piece_height)
        draggable_pieces["bpawn4"] = draggable_bpawn4
        draggable_bpawn5 = DraggablePiece(screen, "./images/200px-Chess_pdt45.svg.png", Board.convert_x_y(4, 1), piece_width, piece_height)
        draggable_pieces["bpawn5"] = draggable_bpawn5
        draggable_bpawn6 = DraggablePiece(screen, "./images/200px-Chess_pdt45.svg.png", Board.convert_x_y(5, 1), piece_width, piece_height)
        draggable_pieces["bpawn6"] = draggable_bpawn6
        draggable_bpawn7 = DraggablePiece(screen, "./images/200px-Chess_pdt45.svg.png", Board.convert_x_y(6, 1), piece_width, piece_height)
        draggable_pieces["bpawn7"] = draggable_bpawn7
        draggable_bpawn8 = DraggablePiece(screen, "./images/200px-Chess_pdt45.svg.png", Board.convert_x_y(7, 1), piece_width, piece_height)
        draggable_pieces["bpawn8"] = draggable_bpawn8
        
        return draggable_pieces
    
    @staticmethod
    def treat_draggable_piece(draggable_piece, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            if draggable_piece.x+piece_width >= mx and draggable_piece.y+piece_height >= my:
                if draggable_piece.x <= mx and draggable_piece.y <= my:
                    draggable_piece.click = True
        elif event.type == pygame.MOUSEBUTTONUP:
            draggable_piece.xshiftbegin = -1
            draggable_piece.yshiftbegin = -1
            draggable_piece.click = False
        elif event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
    
    def play(self):
        state = self.game.state
        player = state.player
        board = state.board
        move = None
        sq2 = ""
        piece = None
        
        if player.ptype == "Human":
            return
        
        move = player.enter_move(game, state.check)
        
        if move == None:
            return
        
        move_entered = True
        