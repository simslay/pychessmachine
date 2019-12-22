import os,sys
import pygame
from board.board import Board

piece_width = 80
piece_height = 80
window_width = 640
window_height = 640

class DraggablePiece:
    def __init__(self, screen, path):
        self.path = path
        self.x, self.y = screen.get_rect().center
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
            screen.blit(board_image, [0,0])
            self.xshift, self.yshift = mx-self.x, my-self.y
            if self.xshiftbegin == -1 and self.yshiftbegin == -1:
                self.xshiftbegin, self.yshiftbegin = self.xshift, self.yshift
            if self.xshiftbegin != -1 or self.yshiftbegin != -1:
                x, y = mx-self.xshiftbegin, my-self.yshiftbegin
            else:
                x, y = mx-self.xshift, my-self.yshift
            self.x, self.y = x, y
            screen.blit(self.image, (x, y))

def main(screen, draggable_piece):
    game_event_loop(draggable_piece)
    draggable_piece.update(screen)


def game_event_loop(draggable_piece):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            if draggable_piece.x+piece_width >= mx and draggable_piece.y+piece_height >= my:
                if draggable_piece.x <= mx and draggable_piece.y <= my:
                    draggable_piece.click = True
        elif event.type == pygame.MOUSEBUTTONUP:
            draggable_piece.click = False
        elif event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

pygame.init()
screen = pygame.display.set_mode((640, 640))
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
    draggable_piece = DraggablePiece(screen, "./images/200px-Chess_nlt45.svg.png")
    while 1:
        main(screen, draggable_piece)
        pygame.display.update()
        clock.tick(60)
