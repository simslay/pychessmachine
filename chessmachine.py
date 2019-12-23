import os
import pygame
from game.game import Game
from gui.draggablepiece import DraggablePiece
from gui.board import Board

piece_width = 80
piece_height = 80
window_width = 640
window_height = 640
game = Game()
draggable_pieces = {}
pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
board_image = pygame.image.load("./images/board01.png")
board_image = pygame.transform.scale(board_image, (window_width, window_height))
screen.blit(board_image, [0, 0])
pygame.display.set_caption("Chessmachine")
clock = pygame.time.Clock()

def main(screen, draggable_pieces):
    game_event_loop(draggable_pieces)
    for draggable_piece in draggable_pieces.values():
        draggable_piece.update(screen, draggable_pieces, board_image)

def game_event_loop(draggable_pieces):
    for event in pygame.event.get():
        for draggable_piece in draggable_pieces.values():
            Board.treat_draggable_piece(draggable_piece, event)


if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    clock = pygame.time.Clock()
    
    game.state.printBoard()
    board = game.state.board
    
    draggable_pieces = Board.get_draggable_pieces(screen)
    
    while 1:
        main(screen, draggable_pieces)
        pygame.display.update()
        clock.tick(60)
