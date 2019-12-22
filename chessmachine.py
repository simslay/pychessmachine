import os,sys
import pygame
from game.game import Game

piece_width = 80
piece_height = 80
window_width = 640
window_height = 640
game = Game()
draggable_pieces = {}

class DraggablePiece:
    def __init__(self, screen, path, xy):
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
    def update(self, screen):
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

def main(screen, draggable_pieces):
    game_event_loop(draggable_pieces)
    for draggable_piece in draggable_pieces.values():
        draggable_piece.update(screen)

def game_event_loop(draggable_pieces):
    for event in pygame.event.get():
        for draggable_piece in draggable_pieces.values():
            treat_draggable_piece(draggable_piece, event)

def treat_draggable_piece(draggable_piece, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        mx, my = event.pos
        if draggable_piece.x+piece_width >= mx and draggable_piece.y+piece_height >= my:
            if draggable_piece.x <= mx and draggable_piece.y <= my:
                draggable_piece.click = True
    elif event.type == pygame.MOUSEBUTTONUP:
        draggable_piece.click = False
    elif event.type == pygame.QUIT:
        pygame.quit(); sys.exit()

def convert_x_y(x, y):
    return x*piece_width, y*piece_height

def get_draggable_pieces():
    draggable_pieces = {}
    
    # rooks
    draggable_wrook1 = DraggablePiece(screen, "./images/200px-Chess_rlt45.svg.png", convert_x_y(0, 7))
    draggable_pieces["wrook1"] = draggable_wrook1
    draggable_wrook2 = DraggablePiece(screen, "./images/200px-Chess_rlt45.svg.png", convert_x_y(7, 7))
    draggable_pieces["wrook2"] = draggable_wrook2
    draggable_brook1 = DraggablePiece(screen, "./images/200px-Chess_rdt45.svg.png", convert_x_y(0, 0))
    draggable_pieces["brook1"] = draggable_brook1
    draggable_brook2 = DraggablePiece(screen, "./images/200px-Chess_rdt45.svg.png", convert_x_y(7, 0))
    draggable_pieces["brook2"] = draggable_brook2
    
    # bishops
    draggable_wbishop1 = DraggablePiece(screen, "./images/200px-Chess_blt45.svg.png", convert_x_y(2, 7))
    draggable_pieces["wbishop1"] = draggable_wbishop1
    draggable_wbishop2 = DraggablePiece(screen, "./images/200px-Chess_blt45.svg.png", convert_x_y(5, 7))
    draggable_pieces["wbishop2"] = draggable_wbishop2
    draggable_bbishop1 = DraggablePiece(screen, "./images/200px-Chess_bdt45.svg.png", convert_x_y(2, 0))
    draggable_pieces["bbishop1"] = draggable_bbishop1
    draggable_bbishop2 = DraggablePiece(screen, "./images/200px-Chess_bdt45.svg.png", convert_x_y(5, 0))
    draggable_pieces["bbishop2"] = draggable_bbishop2
    
    # knights
    draggable_wknigth1 = DraggablePiece(screen, "./images/200px-Chess_nlt45.svg.png", convert_x_y(1, 7))
    draggable_pieces["wknigth1"] = draggable_wknigth1
    draggable_wknigth2 = DraggablePiece(screen, "./images/200px-Chess_nlt45.svg.png", convert_x_y(6, 7))
    draggable_pieces["wknigth2"] = draggable_wknigth2
    draggable_bknigth1 = DraggablePiece(screen, "./images/200px-Chess_ndt45.svg.png", convert_x_y(1, 0))
    draggable_pieces["bknigth1"] = draggable_bknigth1
    draggable_bknigth2 = DraggablePiece(screen, "./images/200px-Chess_ndt45.svg.png", convert_x_y(6, 0))
    draggable_pieces["bknigth2"] = draggable_bknigth2
    
    # queens
    draggable_wqueen = DraggablePiece(screen, "./images/200px-Chess_qlt45.svg.png", convert_x_y(3, 7))
    draggable_pieces["wqueen"] = draggable_wqueen
    draggable_bqueen = DraggablePiece(screen, "./images/200px-Chess_qdt45.svg.png", convert_x_y(3, 0))
    draggable_pieces["bqueen"] = draggable_bqueen
    
    # kings
    draggable_wking = DraggablePiece(screen, "./images/200px-Chess_klt45.svg.png", convert_x_y(4, 7))
    draggable_pieces["wking"] = draggable_wking
    draggable_bking = DraggablePiece(screen, "./images/200px-Chess_kdt45.svg.png", convert_x_y(4, 0))
    draggable_pieces["bking"] = draggable_bking
    
    # pawns
    draggable_wpawn1 = DraggablePiece(screen, "./images/200px-Chess_plt45.svg.png", convert_x_y(0, 6))
    draggable_pieces["wpawn1"] = draggable_wpawn1
    draggable_wpawn2 = DraggablePiece(screen, "./images/200px-Chess_plt45.svg.png", convert_x_y(1, 6))
    draggable_pieces["wpawn2"] = draggable_wpawn2
    draggable_wpawn3 = DraggablePiece(screen, "./images/200px-Chess_plt45.svg.png", convert_x_y(2, 6))
    draggable_pieces["wpawn3"] = draggable_wpawn3
    draggable_wpawn4 = DraggablePiece(screen, "./images/200px-Chess_plt45.svg.png", convert_x_y(3, 6))
    draggable_pieces["wpawn4"] = draggable_wpawn4
    draggable_wpawn5 = DraggablePiece(screen, "./images/200px-Chess_plt45.svg.png", convert_x_y(4, 6))
    draggable_pieces["wpawn5"] = draggable_wpawn5
    draggable_wpawn6 = DraggablePiece(screen, "./images/200px-Chess_plt45.svg.png", convert_x_y(5, 6))
    draggable_pieces["wpawn6"] = draggable_wpawn6
    draggable_wpawn7 = DraggablePiece(screen, "./images/200px-Chess_plt45.svg.png", convert_x_y(6, 6))
    draggable_pieces["wpawn7"] = draggable_wpawn7
    draggable_wpawn8 = DraggablePiece(screen, "./images/200px-Chess_plt45.svg.png", convert_x_y(7, 6))
    draggable_pieces["wpawn8"] = draggable_wpawn8
    
    draggable_bpawn1 = DraggablePiece(screen, "./images/200px-Chess_pdt45.svg.png", convert_x_y(0, 1))
    draggable_pieces["bpawn1"] = draggable_bpawn1
    draggable_bpawn2 = DraggablePiece(screen, "./images/200px-Chess_pdt45.svg.png", convert_x_y(1, 1))
    draggable_pieces["bpawn2"] = draggable_bpawn2
    draggable_bpawn3 = DraggablePiece(screen, "./images/200px-Chess_pdt45.svg.png", convert_x_y(2, 1))
    draggable_pieces["bpawn3"] = draggable_bpawn3
    draggable_bpawn4 = DraggablePiece(screen, "./images/200px-Chess_pdt45.svg.png", convert_x_y(3, 1))
    draggable_pieces["bpawn4"] = draggable_bpawn4
    draggable_bpawn5 = DraggablePiece(screen, "./images/200px-Chess_pdt45.svg.png", convert_x_y(4, 1))
    draggable_pieces["bpawn5"] = draggable_bpawn5
    draggable_bpawn6 = DraggablePiece(screen, "./images/200px-Chess_pdt45.svg.png", convert_x_y(5, 1))
    draggable_pieces["bpawn6"] = draggable_bpawn6
    draggable_bpawn7 = DraggablePiece(screen, "./images/200px-Chess_pdt45.svg.png", convert_x_y(6, 1))
    draggable_pieces["bpawn7"] = draggable_bpawn7
    draggable_bpawn8 = DraggablePiece(screen, "./images/200px-Chess_pdt45.svg.png", convert_x_y(7, 1))
    draggable_pieces["bpawn8"] = draggable_bpawn8
    
    return draggable_pieces

pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Chessmachine")
clock = pygame.time.Clock()

board_image = pygame.image.load("./images/board01.png")
board_image = pygame.transform.scale(board_image, (window_width, window_height))
screen.blit(board_image, [0, 0])

if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    clock = pygame.time.Clock()
    
    game.state.printBoard()
    board = game.state.board
    
    draggable_pieces = get_draggable_pieces()
    
    while 1:
        main(screen, draggable_pieces)
        pygame.display.update()
        clock.tick(60)
