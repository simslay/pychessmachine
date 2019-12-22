import os,sys
import pygame
from board.board import Board
from board.state import State

piece_width = 80
piece_height = 80
window_width = 640
window_height = 640
state = State()
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
    
    draggable_wknigth1 = DraggablePiece(screen, "./images/200px-Chess_nlt45.svg.png", convert_x_y(1, 7))
    draggable_pieces["wknigth1"] = draggable_wknigth1
    draggable_wknigth2 = DraggablePiece(screen, "./images/200px-Chess_nlt45.svg.png", convert_x_y(6, 7))
    draggable_pieces["wknigth2"] = draggable_wknigth2
    
    return draggable_pieces

pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Chessmachine")
clock = pygame.time.Clock()

board = Board()
board.createBoard()
board.printBoard()

board_image = pygame.image.load("./images/board01.png")
board_image = pygame.transform.scale(board_image, (window_width, window_height))
screen.blit(board_image, [0, 0])

if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    clock = pygame.time.Clock()
    board = state.board
    
    draggable_pieces = get_draggable_pieces()
    
    while 1:
        main(screen, draggable_pieces)
        pygame.display.update()
        clock.tick(60)
