import os
import pygame
from gui.board import Board

piece_width = 80
piece_height = 80
window_width = 640
window_height = 640
pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
board_image = pygame.image.load("./images/board01.png")
board_image = pygame.transform.scale(board_image, (window_width, window_height))
screen.blit(board_image, [0, 0])
pygame.display.set_caption("Chessmachine")
clock = pygame.time.Clock()
gui_board = None

def main(screen, draggable_pieces):
    for event in pygame.event.get():
        for i in range(32):
            draggable_piece = draggable_pieces[i]
            if draggable_piece != None:
                gui_board.treat_draggable_piece(screen, draggable_piece, event)

    for draggable_piece in draggable_pieces:
        if draggable_piece != None:
            draggable_piece.update(screen, draggable_pieces, board_image)

if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    clock = pygame.time.Clock()
    
    gui_board = Board(screen, board_image, "Human", "Artificial")
    gui_board.game.state.printBoard()
    state_board = gui_board.game.state.board
    
    while 1:
        main(screen, gui_board.pieces)
        pygame.display.update()
        clock.tick(60)
