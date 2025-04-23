import pygame
from constants import *

def draw_pieces(screen, board, piece_images):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            piece = board[row][col]
            if piece:
                screen.blit(piece_images[piece.color][type(piece)], 
                          (col*SQUARE_SIZE, row*SQUARE_SIZE))

def draw_highlights(screen, moves):
    for move in moves:
        pygame.draw.circle(screen, (255,255,0), 
                         (int((move[1]+0.5)*SQUARE_SIZE), 
                          int((move[0]+0.5)*SQUARE_SIZE)), 
                         int(SQUARE_SIZE/6))

def show_credits(screen):
    font = pygame.font.SysFont('arial', 20)
    text = font.render("Created by Sasank Lama", True, (255,255,255))
    screen.blit(text, (10, WINDOW_SIZE-30))

def draw_game_over(screen):
    font = pygame.font.SysFont('arial', 50)
    text = font.render("Checkmate!", True, (255,0,0))
    screen.blit(text, (WINDOW_SIZE//2-100, WINDOW_SIZE//2-25))
