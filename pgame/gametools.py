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
    message = ""
    def __init__(self):
        pass
    
    @staticmethod
    def convert_x(square, p_size, offset):
        return (ord(square[0]) - ord('a')) * p_size + offset
    
    @staticmethod
    def convert_y(square, p_size, offset):
        return abs(int(square[1]) - 8) * p_size + offset
    
    @staticmethod
    def square(px, py):
        x = chr(ord('a')+int(px/80))
        y = 8-int(py/80)

        return str(x) + str(y)
    
    @staticmethod
    def is_end_of_game(game):
        game.state.check = False

        return    (GameTools.white_is_checkmate(game) or
                  GameTools.black_is_checkmate(game) or
                  GameTools.white_is_stalemate(game) or
                  GameTools.black_is_stalemate(game))
    
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
                    list.append((square1, (i, j)))

#        print("valid_moves() --->")
#        #game.state.printBoard()
#        print("valid_moves() : player.alliance = " + player.alliance)
#        print("valid_moves() : check = " + str(check))
#        print("valid_moves() : p = " + str(p))
#        print("valid_moves() : square1 = " + str(square1))
#        for move in list:
#            print("valid_moves() : move = " + str(move))
#        print("valid_moves() <---")
        return list
    
    @staticmethod
    def white_is_stalemate(game):
        game_state = game.state
        state_copy = None
        player = game_state.player
        white_pieces = game_state.white_pieces
        piece = None
        valid_moves = None
        move = None

        if player.alliance == "Blacks":
            return False

        for i in range(16):
            piece = white_pieces[i]
            
            if piece != None:
                valid_moves = GameTools.valid_moves(game, piece, True)
                
                for j in range(len(valid_moves)):
                    move = valid_moves[j]

                    state_copy = pgame.state.State(game_state)
                    
                    if state_copy == None:
                        return False
                    
                    game.verify_and_play_move(state_copy, move[0][0], move[0][1], move[1][0], move [1][1], True)
                    if not GameTools.white_is_check(game, state_copy, state_copy.wking.x, state_copy.wking.y):
                        return False

        GameTools.message = "Whites are stalemated!"
        print(GameTools.message)
        
        return True
    
    @staticmethod
    def black_is_stalemate(game):
        game_state = game.state
        state_copy = None
        player = game_state.player
        black_pieces = game_state.black_pieces
        piece = None
        valid_moves = None
        move = None

        if player.alliance == "Whites":
            return False
        
        for i in range(16):
            piece = black_pieces[i]
            
            if piece != None:
                valid_moves = GameTools.valid_moves(game, piece, True)
                
                for j in range(len(valid_moves)):
                    move = valid_moves[j]
                    state_copy = pgame.state.State(game_state)
                    
                    if state_copy == None:
                        return False
                    
                    game.verify_and_play_move(state_copy, move[0][0], move[0][1], move[1][0], move[1][1], True)
                    
                    if not GameTools.black_is_check(game, state_copy, state_copy.bking.x, state_copy.bking.y):
                        return False
        
        GameTools.message = "Blacks are stalemated!"
        print(GameTools.message)
        
        return True

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
        white_piece = None

        for i in range(16):
            white_piece = white_pieces[i]

            if white_piece != None:
                if white_piece.is_valid_move(white_piece.x, white_piece.y, x, y, board, game.whites_player, False):
#                    print("black_is_check() -> white_piece.is_valid_move() == True")
#                    print("black_is_check() : white_piece = " + str(white_piece))
#                    print("black_is_check() : white_piece.x, white_piece.y = " + str((white_piece.x, white_piece.y)))
#                    print("black_is_check() : x, y = ", str((x, y)))
                    return True

        return False
    
    @staticmethod
    def white_is_checkmate(game):
        game_state = game.state
        state_copy = None
        wKing = game_state.wking
        x = wKing.x
        y = wKing.y
        white_pieces = game_state.white_pieces
        valid_moves = []
        move = []

        state_copy = pgame.state.State(game_state)

        if game.state.player.alliance == "Blacks":
            if GameTools.white_is_check(game, state_copy, x, y):
                GameTools.message = "Whites will be check!"
                print(GameTools.message)
                game_state.player = GameTools.change_player(game_state.player, game)
                return True
            return False

        state_copy = pgame.state.State(game_state)

        if GameTools.white_is_check(game, state_copy, x, y):

            for i in range(16):
                valid_moves = GameTools.valid_moves(game, white_pieces[i], True)
                if len(valid_moves) == 0:
                    continue

                for j in range(len(valid_moves)):
                    move = valid_moves[j]
                    state_copy = pgame.state.State(game_state)

                    if state_copy == None:
                        return False

                    game.verify_and_play_move(state_copy, move[0][0], move[0][1], move[1][0], move [1][1], True)

                    if not GameTools.white_is_check(game, state_copy, state_copy.wking.x, state_copy.wking.y):
                        GameTools.message = "Check!"
                        print(GameTools.message)
                        game_state.check = True
                        return False
            GameTools.message = "Checkmate! Blacks win"
            print(GameTools.message)
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
        
        #print("black_is_checkmate() : bking.x=" + str(bking.x) + ", bking.y=" + str(bking.y))

        state_copy = pgame.state.State(state)

        if game.state.player.alliance == "Whites":
            if GameTools.black_is_check(game, state_copy, x, y):
                GameTools.message = "Blacks will be check!"
                print(GameTools.message)
                state.player = GameTools.change_player(state.player, game)
                return True
            return False

        state_copy = pgame.state.State(state)
        
        if GameTools.black_is_check(game, state_copy, x, y):
            for i in range(16):
                valid_moves = GameTools.valid_moves(game, black_pieces[i], True)
                if len(valid_moves) == 0:
                    continue

                for j in range(len(valid_moves)):
                    move = valid_moves[j]
                    state_copy = pgame.state.State(state)

                    if state_copy == None:
                        return False

                    game.verify_and_play_move(state_copy, move[0][0], move[0][1], move[1][0], move[1][1], True)

                    if not GameTools.black_is_check(game, state_copy, state_copy.bking.x, state_copy.bking.y):
                        GameTools.message = "Check!"
                        print(GameTools.message)
                        state.check = True
                        
                        return False

            #state_copy.printBoard()
            GameTools.message = "Checkmate! Whites win"
            print(GameTools.message)
            
            return True
        return False

    @staticmethod
    def change_player(player, game):
        if player.alliance == "Whites":
            return game.blacks_player
        elif player.alliance == "Blacks":
            return game.whites_player
