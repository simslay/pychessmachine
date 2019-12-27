# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 11:17:33 2019

@author: simslay
"""

import sys
import pygame
from gui.draggablepiece import DraggablePiece
from pgame.game import Game
from pgame.gametools import GameTools
from pgame.pieces.bishop import Bishop
from pgame.pieces.knight import Knight
from pgame.pieces.queen import Queen
from pgame.pieces.rook import Rook
from pgame.state import State

piece_width = 80
piece_height = 80

class Board():
    game = None
    move_entered = None
    square1 = ""
    square2 = ""
    p_size = 80
    offset = 0
    pieces = None
    selected_piece = None
    xcurs = None
    ycurs = None
    select = False
    end_of_game = None
    # images des pieces blanches
    wht_pwn_img = None
    wht_rk_img = None
    wht_knt_img = None
    wht_bsp_img = None
    wht_qn_img = None
    wht_kng_img = None
    # images des pieces noires
    blk_pwn_img = None
    blk_rk_img = None
    blk_knt_img = None
    blk_bsp_img = None
    blk_qn_img = None
    blk_kng_img = None
    imax = 1000
    begin = True
    xi = None
    yi = None
    board_image = None
    
    def __init__(self, screen, board_image, wtype, btype):
        self.game = Game(wtype, btype)
        self.end_of_game = False
        self.init(screen)
        self.xi = 0
        self.yi = 0
        self.board_image = board_image
        
    @staticmethod
    def convert_x_y(x, y):
        return x*piece_width, y*piece_height

    def init(self, screen):
        draggable_pieces = []
        
        # rooks
        draggable_wrook1 = DraggablePiece(screen, "rok", "Whites", "./images/200px-Chess_rlt45.svg.png", Board.convert_x_y(0, 7), piece_width, piece_height)
        self.wht_rk_img = draggable_wrook1.image
        draggable_pieces.append(draggable_wrook1)
        draggable_wrook2 = DraggablePiece(screen, "rok", "Whites", "./images/200px-Chess_rlt45.svg.png", Board.convert_x_y(7, 7), piece_width, piece_height)
        draggable_pieces.append(draggable_wrook2)
        draggable_brook1 = DraggablePiece(screen, "rok", "Blacks", "./images/200px-Chess_rdt45.svg.png", Board.convert_x_y(0, 0), piece_width, piece_height)
        self.blk_rk_img = draggable_brook1.image
        draggable_pieces.append(draggable_brook1)
        draggable_brook2 = DraggablePiece(screen, "rok", "Blacks", "./images/200px-Chess_rdt45.svg.png", Board.convert_x_y(7, 0), piece_width, piece_height)
        draggable_pieces.append(draggable_brook2)
        
        # bishops
        draggable_wbishop1 = DraggablePiece(screen, "bsp", "Whites", "./images/200px-Chess_blt45.svg.png", Board.convert_x_y(2, 7), piece_width, piece_height)
        self.wht_bsp_img = draggable_wbishop1.image
        draggable_pieces.append(draggable_wbishop1)
        draggable_wbishop2 = DraggablePiece(screen, "bsp", "Whites", "./images/200px-Chess_blt45.svg.png", Board.convert_x_y(5, 7), piece_width, piece_height)
        draggable_pieces.append(draggable_wbishop2)
        draggable_bbishop1 = DraggablePiece(screen, "bsp", "Blacks", "./images/200px-Chess_bdt45.svg.png", Board.convert_x_y(2, 0), piece_width, piece_height)
        self.blk_bsp_img = draggable_bbishop1.image
        draggable_pieces.append(draggable_bbishop1)
        draggable_bbishop2 = DraggablePiece(screen, "bsp", "Blacks", "./images/200px-Chess_bdt45.svg.png", Board.convert_x_y(5, 0), piece_width, piece_height)
        draggable_pieces.append(draggable_bbishop2)
        
        # knights
        draggable_wknigth1 = DraggablePiece(screen, "knt", "Whites", "./images/200px-Chess_nlt45.svg.png", Board.convert_x_y(1, 7), piece_width, piece_height)
        self.wht_knt_img = draggable_wknigth1.image
        draggable_pieces.append(draggable_wknigth1)
        draggable_wknigth2 = DraggablePiece(screen, "knt", "Whites", "./images/200px-Chess_nlt45.svg.png", Board.convert_x_y(6, 7), piece_width, piece_height)
        draggable_pieces.append(draggable_wknigth2)
        draggable_bknigth1 = DraggablePiece(screen, "knt", "Blacks", "./images/200px-Chess_ndt45.svg.png", Board.convert_x_y(1, 0), piece_width, piece_height)
        self.blk_knt_img = draggable_bknigth1.image
        draggable_pieces.append(draggable_bknigth1)
        draggable_bknigth2 = DraggablePiece(screen, "knt", "Blacks", "./images/200px-Chess_ndt45.svg.png", Board.convert_x_y(6, 0), piece_width, piece_height)
        draggable_pieces.append(draggable_bknigth2)
        
        # queens
        draggable_wqueen = DraggablePiece(screen, "qun", "Whites", "./images/200px-Chess_qlt45.svg.png", Board.convert_x_y(3, 7), piece_width, piece_height)
        self.wht_qn_img = draggable_wqueen.image
        draggable_pieces.append(draggable_wqueen)
        draggable_bqueen = DraggablePiece(screen, "qun", "Blacks", "./images/200px-Chess_qdt45.svg.png", Board.convert_x_y(3, 0), piece_width, piece_height)
        self.blk_qn_img = draggable_bqueen.image
        draggable_pieces.append(draggable_bqueen)
        
        # kings
        draggable_wking = DraggablePiece(screen, "kng", "Whites", "./images/200px-Chess_klt45.svg.png", Board.convert_x_y(4, 7), piece_width, piece_height)
        self.wht_kng_img = draggable_wking.image
        draggable_pieces.append(draggable_wking)
        draggable_bking = DraggablePiece(screen, "kng", "Blacks", "./images/200px-Chess_kdt45.svg.png", Board.convert_x_y(4, 0), piece_width, piece_height)
        self.blk_kng_img = draggable_bking.image
        draggable_pieces.append(draggable_bking)
        
        # pawns
        draggable_wpawn1 = DraggablePiece(screen, "pwn", "Whites", "./images/200px-Chess_plt45.svg.png", Board.convert_x_y(0, 6), piece_width, piece_height)
        self.wht_pwn_img = draggable_wpawn1.image
        draggable_pieces.append(draggable_wpawn1)
        draggable_wpawn2 = DraggablePiece(screen, "pwn", "Whites", "./images/200px-Chess_plt45.svg.png", Board.convert_x_y(1, 6), piece_width, piece_height)
        draggable_pieces.append(draggable_wpawn2)
        draggable_wpawn3 = DraggablePiece(screen, "pwn", "Whites", "./images/200px-Chess_plt45.svg.png", Board.convert_x_y(2, 6), piece_width, piece_height)
        draggable_pieces.append(draggable_wpawn3)
        draggable_wpawn4 = DraggablePiece(screen, "pwn", "Whites", "./images/200px-Chess_plt45.svg.png", Board.convert_x_y(3, 6), piece_width, piece_height)
        draggable_pieces.append(draggable_wpawn4)
        draggable_wpawn5 = DraggablePiece(screen, "pwn", "Whites", "./images/200px-Chess_plt45.svg.png", Board.convert_x_y(4, 6), piece_width, piece_height)
        draggable_pieces.append(draggable_wpawn5)
        draggable_wpawn6 = DraggablePiece(screen, "pwn", "Whites", "./images/200px-Chess_plt45.svg.png", Board.convert_x_y(5, 6), piece_width, piece_height)
        draggable_pieces.append(draggable_wpawn6)
        draggable_wpawn7 = DraggablePiece(screen, "pwn", "Whites", "./images/200px-Chess_plt45.svg.png", Board.convert_x_y(6, 6), piece_width, piece_height)
        draggable_pieces.append(draggable_wpawn7)
        draggable_wpawn8 = DraggablePiece(screen, "pwn", "Whites", "./images/200px-Chess_plt45.svg.png", Board.convert_x_y(7, 6), piece_width, piece_height)
        draggable_pieces.append(draggable_wpawn8)
        
        draggable_bpawn1 = DraggablePiece(screen, "pwn", "Blacks", "./images/200px-Chess_pdt45.svg.png", Board.convert_x_y(0, 1), piece_width, piece_height)
        self.blk_pwn_img = draggable_bpawn1.image
        draggable_pieces.append(draggable_bpawn1)
        draggable_bpawn2 = DraggablePiece(screen, "pwn", "Blacks", "./images/200px-Chess_pdt45.svg.png", Board.convert_x_y(1, 1), piece_width, piece_height)
        draggable_pieces.append(draggable_bpawn2)
        draggable_bpawn3 = DraggablePiece(screen, "pwn", "Blacks", "./images/200px-Chess_pdt45.svg.png", Board.convert_x_y(2, 1), piece_width, piece_height)
        draggable_pieces.append(draggable_bpawn3)
        draggable_bpawn4 = DraggablePiece(screen, "pwn", "Blacks", "./images/200px-Chess_pdt45.svg.png", Board.convert_x_y(3, 1), piece_width, piece_height)
        draggable_pieces.append(draggable_bpawn4)
        draggable_bpawn5 = DraggablePiece(screen, "pwn", "Blacks", "./images/200px-Chess_pdt45.svg.png", Board.convert_x_y(4, 1), piece_width, piece_height)
        draggable_pieces.append(draggable_bpawn5)
        draggable_bpawn6 = DraggablePiece(screen, "pwn", "Blacks", "./images/200px-Chess_pdt45.svg.png", Board.convert_x_y(5, 1), piece_width, piece_height)
        draggable_pieces.append(draggable_bpawn6)
        draggable_bpawn7 = DraggablePiece(screen, "pwn", "Blacks", "./images/200px-Chess_pdt45.svg.png", Board.convert_x_y(6, 1), piece_width, piece_height)
        draggable_pieces.append(draggable_bpawn7)
        draggable_bpawn8 = DraggablePiece(screen, "pwn", "Blacks", "./images/200px-Chess_pdt45.svg.png", Board.convert_x_y(7, 1), piece_width, piece_height)
        draggable_pieces.append(draggable_bpawn8)
        
        self.pieces = draggable_pieces
    
    def treat_draggable_piece(self, screen, draggable_piece, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            if draggable_piece.x + piece_width >= mx and draggable_piece.y+piece_height >= my:
                if draggable_piece.x <= mx and draggable_piece.y <= my:
                    draggable_piece.click = True
            
            # Java import (begin) #
            if (self.game.state.player.ptype == "Artificial"):
                return
            
            self.begin = False
            self.xcurs = mx
            self.ycurs = my
            self.square1 = GameTools.square(self.xcurs - self.offset, self.ycurs - self.offset)

            if draggable_piece != None:
                if (self.xcurs > draggable_piece.x and self.xcurs < draggable_piece.x + self.p_size and
                    self.ycurs > draggable_piece.y and self.ycurs < draggable_piece.y + self.p_size):
                    self.select = True
                    draggable_piece.selected = True
                    self.selected_piece = draggable_piece
                    
#                   if (positionLabel!=null)
#                       positionLabel.setText(GameUtil.square(xcurs-offset, ycurs-offset));
            # Java import (end)
        elif event.type == pygame.MOUSEBUTTONUP:
            mx, my = event.pos
            draggable_piece.xshiftbegin = -1
            draggable_piece.yshiftbegin = -1
            draggable_piece.click = False
            
            # Java import (begin) #
            if self.game.state.player.ptype == "Human":
                self.play_move(screen, mx, my)
            # Java import (end) #
        elif event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
    
    def play(self, screen):
        state = self.game.state
        player = state.player
        board = state.board
        move = None
        sq2 = ""
        piece = None
        
        if player.ptype == "Human":
            return
        
        move = player.enter_move(self.game, state.check) # ((x1, y1), (x2, y2))
        
        if move == None:
            return
        
        self.move_entered = True
        self.square1 = "" + (chr(ord("a") + move[0][0])) + str(abs(move[0][1]-8))
        sq2 = "" + (chr(ord("a") + move[1][0])) + str(abs(move[1][1]-8))
        print("CPU tries " + sq2)
        
        for i in range(32):
            if (self.pieces[i] != None and
                self.pieces[i].x == GameTools.convert_x(self.square1, self.p_size, self.offset) and
                self.pieces[i].y == GameTools.convert_y(self.square1, self.p_size, self.offset)):
                self.pieces[i].selected = True
                self.selected_piece = self.pieces[i]
                # promotion
                if len(move) == 3:
                    for j in range(16):
                        if state.white_pieces[j] != None and state.white_pieces[j].promoted:
                            state.white_pieces[j].promoted = False
                        if state.black_pieces[j] != None and state.black_pieces[j].promoted:
                            state.black_pieces[j].promoted = False

                    piece = board[move[0][1]][move[0][0]]
                    board[move[0][1]][move[0][0]] = None

                    if move[2][0] == 0:
                        board[move[0][1]][move[0][0]] = Queen(player.alliance)
                    elif move[2][0] == 1:
                        board[move[0][1]][move[0][0]] = Rook(player.alliance)
                    elif move[2][0] == 2:
                        board[move[0][1]][move[0][0]] = Bishop(player.alliance)
                    elif move[2][0] == 3:
                        board[move[0][1]][move[0][0]] = Knight(player.alliance)
                    else:
                        board[move[0][1]][move[0][0]] = Queen(player.alliance)

                    board[move[0][1]][move[0][0]].promoted = True

                    if player.alliance == "Whites":
                        for j in range(16):
                            if (state.white_pieces[j] != None and
                                hash(state.white_pieces[j]) == hash(piece)):
                                state.white_pieces[j] = board[move[0][1]][move[0][0]]
                                break
                    elif player.alliance == "Blacks":
                        for j in range(16):
                            if (state.black_pieces[j] != None and
                                hash(state.black_pieces[j]) == hash(piece)):
                                state.black_pieces[j] = board[move[0][1]][move[0][0]]
                                break
                break
            if i+1 == 32:
                return

        self.play_move(screen, GameTools.convert_x(sq2, self.p_size, self.offset), GameTools.convert_y(sq2, self.p_size, self.offset))
        
    def play_move(self, screen, x, y):
        #print("play_move(" + str(x) + ", " + str(y) + ")")
        if self.game.state.player.ptype == "Artificial" and not self.move_entered:
            return
        else:
            self.move_entered = False
        
        for i in range(32):
            if self.pieces[i] != None and self.pieces[i].selected:
                break
            if i+1 == 32:
                return
        
        game_state = self.game.state
        next_state = None
        self.xcurs = x
        self.ycurs = y
        y1 = abs(int(self.square1[1])-8)
        x1 = ord(self.square1[0])-ord('a')
        y2 = None
        x2 = None
        current_player = self.game.state.player
        piece = self.game.state.board[y1][x1]
        
        print("play_move() : x1=" + str(x1) + ", y1=" + str(y1))
        print("play_move() : piece = " + str(piece))

        if piece == None:
            return
        
        next_state = State(game_state)

        if pygame.mouse.get_focused() == 0 and current_player.ptype != "Artificial":
            self.selected_piece.x = GameTools.convertX(self.square1, self.p_size, self.offset)
            self.selected_piece.y = GameTools.convertY(self.square1, self.p_size, self.offset)
            self.selected_piece.selected = False
            self.paint(screen)
            return

        self.select = False
        self.square2 = GameTools.square(self.xcurs-self.offset, self.ycurs-self.offset)
        y2 = abs(int(self.square2[1])-8)
        x2 = ord(self.square2[0]) - ord('a')
            
        if self.game.verify_and_play_move(next_state, x1, y1, x2, y2, False) and not self.end_of_game:
            self.game.state = next_state
            if not GameTools.is_end_of_game(self.game):
                    
                # placement de la piece
                self.selected_piece.x = GameTools.convert_x(self.square2, self.p_size, self.offset)
                self.selected_piece.y = GameTools.convert_y(self.square2, self.p_size, self.offset)
                self.selected_piece.selected = False
                    
                n = 0

                for i in range(8):
                    for j in range(8):
                        p = self.game.state.board[j][i]

                        if p != None:

                            for k in range(32):
                                if (self.pieces[k] != None and
                                    self.pieces[k].selected == False):
                                        
                                    self.change_image(self.pieces[k], p)
                                        
                                    self.pieces[k].x = GameTools.convert_x(str(chr(i + ord('a'))) + str(abs(j-8)), self.p_size, self.offset)
                                    self.pieces[k].y = GameTools.convert_y(str(chr(i + ord('a'))) + str(abs(j-8)), self.p_size, self.offset)
                                    self.pieces[k].selected = True
                                    n = k+1
                                    break
                for k in range(n, 32):
                    if self.pieces[k] != None and self.pieces[k].selected == False:
                        self.pieces[k] = None
                    
                self.game.state.review.append((self.square1, self.square2))
            else:
                if (GameTools.message == "White will be check!" or
                    GameTools.message == "Black will be check!"):
                    self.game.state = game_state
                    for i in range(32):
                        if self.pieces[i] != None and self.pieces[i].selected:
                            self.pieces[i].selected = False
                            self.pieces[i].x = GameTools.convert_x(self.square1, self.p_size, self.offset)
                            self.pieces[i].y = GameTools.convert_y(self.square1, self.p_size, self.offset)
                            break
                elif (GameTools.message == "Checkmate! White wins" or
                        GameTools.message == "Checkmate! Black wins" or
                        GameTools.message == "White is stalemated!" or
                        GameTools.message == "Black is stalemated!"):
                    self.end_of_game = True
                    self.imax = 0
                        
                    # capture et/ou placement du dernier coup
                    self.selected_piece.x = GameTools.convert_x(self.square2, self.p_size, self.offset)
                    self.selected_piece.y = GameTools.convert_y(self.square2, self.p_size, self.offset)
                    self.selected_piece.selected = False
                        
                    n = 0

                    for i in range(8):
                        for j in range(8):
                            p = self.game.state.board[j][i]
                            if p != None:

                                for k in range(32):
                                    if (self.pieces[k] != None and
                                        self.pieces[k].selected == False):
                            
                                        self.change_image(self.pieces[k], p)
                                        
                                        self.pieces[k].x = GameTools.convert_x(str(chr(i + ord('a'))) + str(abs(j-8)), self.p_size, self.offset)
                                        self.pieces[k].y = GameTools.convert_y(str(chr(i + ord('a'))) + str(abs(j-8)), self.p_size, self.offset)
                                        self.pieces[k].selected = True
                                        n = k+1
                                        break
                    for k in range(n, 32):
                        if self.pieces[k] != None and self.pieces[k].selected == False:
                            self.pieces[k] = None
        
                    self.game.state.review.append((self.square1, self.square2))
            self.paint(screen)
        else:
            if not self.end_of_game:
                self.game.state = next_state
    
            player = "Whites" if piece.alliance == "Whites" else "Blacks"
    
            if piece.alliance == current_player.alliance and not self.end_of_game:
                print("Move is not valid")
            elif not self.end_of_game:
                print("This is not " + player + " turn")
    
            self.selected_piece.selected = False
            self.selected_piece.x = GameTools.convert_x(self.square1, self.p_size, self.offset)
            self.selected_piece.y = GameTools.convert_y(self.square1, self.p_size, self.offset)
                
            self.paint(screen)
        
        for i in range(32):
            if self.pieces[i] != None:
                self.pieces[i].selected = False
        
        p = None
        
        if next_state.player.alliance == "Whites":
            p = self.game.blacks_player
        else:
            p = self.game.whites_player
        
        if (next_state.player.ptype == "Artificial" and
            p.ptype == "Human" and
            not self.end_of_game):
            self.play(screen)
    
    def paint(self, screen):
        # affichage de l'echiquier
        screen.blit(self.board_image, (0, 0))
        
        # affichage des images des pieces
        for i in range(32):
            if self.pieces[i] != None:
                if self.pieces[i].selected or self.begin:
                    screen.blit(self.pieces[i].image, (self.pieces[i].x + self.xi, self.pieces[i].y + self.yi))
                    
                    self.pieces[i].x = self.pieces[i].x + self.xi
                    self.pieces[i].y = self.pieces[i].y + self.yi
                else:
                    screen.blit(self.pieces[i].image, (self.pieces[i].x, self.pieces[i].y))

    def change_image(self, pimage, piece):
        nom = piece.nom
        alliance = piece.alliance
        
        if (pimage.nom == nom and
            pimage.alliance == alliance):
            return
        
        pimage.nom = nom
        pimage.alliance = alliance
        
        if alliance == "Whites":
            if nom == "rok":
                pimage.image = self.wht_rk_img
            elif nom == "knt":
                pimage.image = self.wht_knt_img
            elif nom == "bsp":
                pimage.image = self.wht_bsp_img
            elif nom == "qun":
                pimage.image = self.wht_qn_img
            elif nom == "kng":
                pimage.image = self.wht_kng_img
            elif nom == "pwn":
                pimage.image = self.wht_pwn_img
        elif alliance == "Blacks":
            if nom == "rok":
                pimage.image = self.blk_rk_img
            elif nom == "knt":
                pimage.image = self.blk_knt_img
            elif nom == "bsp":
                pimage.image = self.blk_bsp_img
            elif nom == "qun":
                pimage.image = self.blk_qn_img
            elif nom == "kng":
                pimage.image = self.blk_kng_img
            elif nom == "pwn":
                pimage.image = self.blk_pwn_img
