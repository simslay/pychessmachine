# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 11:06:05 2019

@author: simslay
"""

import pygame

class DraggablePiece:
    def __init__(self, screen, path, xy, piece_width, piece_height):
        self.path = path
        self.x, self.y = xy
        self.xshift = 0
        self.yshift = 0
        self.xshiftbegin = -1
        self.yshiftbegin = -1
        self.click = False
        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, (piece_width, piece_height))
        screen.blit(self.image, (self.x, self.y))
    def update(self, screen, draggable_pieces, board_image):
        if self.click:
            mx, my = pygame.mouse.get_pos()
            screen.blit(board_image, [0, 0])
            for draggable_piece in draggable_pieces.values():
                if draggable_piece != self:
                    screen.blit(draggable_piece.image, [draggable_piece.x, draggable_piece.y])
            self.xshift, self.yshift = mx-self.x, my-self.y
            if self.xshiftbegin == -1 and self.yshiftbegin == -1:
                self.xshiftbegin, self.yshiftbegin = self.xshift, self.yshift
            if self.xshiftbegin != -1 or self.yshiftbegin != -1:
                x, y = mx-self.xshiftbegin, my-self.yshiftbegin
            else:
                x, y = mx-self.xshift, my-self.yshift
            self.x, self.y = x, y
            screen.blit(self.image, (x, y))