import pygame
from game_state import GameState
from board import draw_board
from ui import draw_pieces, draw_highlights, show_credits, draw_game_over
from ai import ChessAI
from sound import SoundManager

pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE + 200, WINDOW_SIZE))
clock = pygame.time.Clock()
sound = SoundManager()
piece_images = {
    'white': {
        Pawn: pygame.image.load('assets/white_pawn.png'),
        Rook: pygame.image.load('assets/white_rook.png'),
        Knight: pygame.image.load('assets/white_knight.png'),
        Bishop: pygame.image.load('assets/white_bishop.png'),
        Queen: pygame.image.load('assets/white_queen.png'),
        King: pygame.image.load('assets/white_king.png')
    },
    'black': {
        Pawn: pygame.image.load('assets/black_pawn.png'),
        Rook: pygame.image.load('assets/black_rook.png'),
        Knight: pygame.image.load('assets/black_knight.png'),
        Bishop: pygame.image.load('assets/black_bishop.png'),
        Queen: pygame.image.load('assets/black_queen.png'),
        King: pygame.image.load('assets/black_king.png')
    }
}

