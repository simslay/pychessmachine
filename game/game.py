# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 21:09:10 2019

@author: simslay
"""

from game.state import State
from game.players.whites import Whites
from game.players.blacks import Blacks
from game.pieces.queen import Queen
from game.pieces.rook import Rook
from game.pieces.bishop import Bishop
from game.pieces.knight import Knight
import tkinter as tk
from tkinter.constants import END

class Game():
    state = None
    whites_player = None
    blacks_player = None
    selected_value = None
    listbox = None
    
    def __init__(self):
        self.state = State()
        self.whites_player = Whites()
        self.blacks_player = Blacks()
        
        self.state.player = self.whites_player
        
    def verify_and_play_move(self, state, x1, y1, x2, y2, test):
        board = state.board
        whites = state.white_pieces
        blacks = state.black_pieces
        current_player = state.player
        
        piece = board[y1][x1]
        
        if piece != None and (piece.is_valid_move(x1, y1, x2, y2, board, current_player, state.checked) or
			(state.player.ptype == "Artificial" and piece.promoted)):
            # enlevement de la piece
            board[y1][x1] = None
            
            if board[y2][x2] == None:
                if current_player.alliance == "Whites":
                    if (x2 == x1+1 or x2 == x1-1) and y1 == 3 and y2 == 2:
                        if board[y2+1][x2] != None and board[y2+1][x2].en_passant_risk:
                            for i in range(16):
                                if blacks[i] != None and hash(blacks[i]) == hash(board[y2+1][x2]):
                                    blacks[i] = None
                                    state.add_capture(board[y2+1][x2])
                                    board[y2+1][x2] = None
                                    break
                    else: # annulation de l'eventuel pion en_passant_risk = true
                        for i in range(16):
                            if blacks[i] != null and blacks[i].en_passant_risk:
                                blacks[i].en_passant_risk = False
                                break
                elif current_player.alliance == "Blacks":
                    if (x2 == x1+1 or x2 == x1-1) and y1 == 4 and y2 == 5:
                        if board[y2-1][x2] != None and board[y2-1][x2].en_passant_risk:
                            for i in range(16):
                                if whites[i] != None and hash(whites[i]) == hash(board[y2-1][x2]):
                                    whites[i] = None
                                    state.add_capture(board[y2-1][x2]);
                                    board[y2-1][x2] = None
                                    break
                    else: # annulation de l'eventuel pion en_passant_risk = true
                        for i in range(16):
                            if whites[i]!=null and whites[i].en_passant_risk:
                                whites[i].en_passant_risk = False
                                break
            elif board[y2][x2] != None:
                state.add_capture(board[y2][x2])
                if currentPlayer.alliance == "Whites":
                    for i in range(16):
                        if blacks[i] != None and hash(blacks[i]) == hash(board[y2][x2]):
                            blacks[i] = None
                            break
                elif current_player.alliance == "Blacks":
                    for i in range(16):
                        if whites[i] != None and hash(whites[i]) == hash(board[y2][x2].hashCode):
                            whites[i] = None
                            break
						
            # placement de la nouvelle piece
            # promotion
            if current_player.ptype != "Artificial":
                for i in range(16):
                    if whites[i] != None and whites[i].promoted:
                        whites[i].promoted = False
                    if blacks[i] != null and blacks[i].promoted:
                        blacks[i].promoted = False

            if (not test and piece.nom == "pwn" and
                current_player.ptype != "Artificial" and
                piece.alliance == "Whites" and
                y2 == 0):
						
                self.listbox = tk.Listbox()
                for item in ["Queen", "Rook", "Bishop", "Knight"]:
                    self.listbox.insert(END, item)
                self.listbox.pack()
                
                listbox.bind("<<ListboxSelect>>", self.select)
                tk.mainloop()
				
                if self.selected_value == None:
                    return False
				
                if selectedValue == 0:
                    board[y2][x2] = Queen("Whites")
                elif selected_value == 1:
                    board[y2][x2] = Rook("Whites")
                elif selected_value == 2:
                    board[y2][x2] = Bishop("Whites")
                elif selected_value == 3:
                    board[y2][x2] = Knight("Whites")
				
                board[y2][x2].x = x2
                board[y2][x2].y = y2
                board[y2][x2].promoted = True
                
                for i in range(16):
                    if whites[i] != None and hash(whites[i]) == hash(piece):
                        whites[i] = board[y2][x2]
                        break				
            elif (not test and piece.nom == "pwn" and
                  current_player.ptype != "Artificial" and
                  piece.alliance == "Blacks" and
                  y2 == 7):

                self.listbox = tk.Listbox()
                for item in ["Queen", "Rook", "Bishop", "Knight"]:
                    self.listbox.insert(END, item)
                self.listbox.pack()
                
                listbox.bind("<<ListboxSelect>>", self.select)
                tk.mainloop()

                if self.selected_value == None:
                    return False
				
                if selectedValue == 0:
                    board[y2][x2] = Queen("Blacks")
                elif selected_value == 1:
                    board[y2][x2] = Rook("Blacks")
                elif selected_value == 2:
                    board[y2][x2] = Bishop("Blacks")
                elif selected_value == 3:
                    board[y2][x2] = Knight("Blacks")

                board[y2][x2].x = x2
                board[y2][x2].y = y2
                board[y2][x2].promoted = True
                
                for i in range(16):
                    if blacks[i] != None and hash(blacks[i]) == hash(piece):
                        blacks[i] = board[y2][x2]
                        break				
            else:
                board[y2][x2] = piece
                piece.x = x2
                piece.y = y2
                
                # castling
                if (not state.check and x1 == 4 and (x2 == 2 or x2 == 6) and
                    ((y1 == 0 and y2 == 0) or (y1 == 7 and y2 == 7))):
                    if board[y2][x2].nom == "kng":
                        if (x2 == 2 and board[y2][0] != None and
                            board[y2][0].nom == "rok" and
                            board[y2][0].castling_poss):
                            
                            board[y2][3] = board[y2][0]
                            board[y2][0] = None
                            board[y2][3].x = 3
                            board[y2][3].y = y2
                            board[y2][3].castling_poss = False
								
                        elif (x2 == 6 and board[y2][7] != None and
                              board[y2][7].nom == "rok" and
                              board[y2][7].castling_poss):

                            board[y2][5] = board[y2][7]
                            board[y2][7] = None
                            board[y2][5].x = 5
                            board[y2][5].y = y2
                            board[y2][5].castling_poss = False									

            # changement du joueur
            state.player = self.change_player(current_player)

            # check
            if state.check:
                state.check = False

            return True
        else:
            return False
    
    def select(self, event):
        self.selected_value = self.listbox.curselection()[0]
    
    def change_player(self, player):
        if player.alliance == "Whites":
            return self.blacks_player
        elif player.alliance == "Blacks":
            return self.whites_player