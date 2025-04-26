from constants import *
from pieces import Pawn, Rook, Knight, Bishop, Queen, King



def create_start_board():
    board = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    
    # Black pieces
    board[0] = [
        Rook(BLACK, (0,0)), Knight(BLACK, (0,1)), Bishop(BLACK, (0,2)), 
        Queen(BLACK, (0,3)), King(BLACK, (0,4)), Bishop(BLACK, (0,5)), 
        Knight(BLACK, (0,6)), Rook(BLACK, (0,7))
    ]
    board[1] = [Pawn(BLACK, (1,c)) for c in range(8)]
    
    # White pieces
    board[7] = [
        Rook(WHITE, (7,0)), Knight(WHITE, (7,1)), Bishop(WHITE, (7,2)), 
        Queen(WHITE, (7,3)), King(WHITE, (7,4)), Bishop(WHITE, (7,5)), 
        Knight(WHITE, (7,6)), Rook(WHITE, (7,7))
    ]
    board[6] = [Pawn(WHITE, (6,c)) for c in range(8)]
    
    return board

def draw_board(screen):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            color = THEME[(row + col) % 2]
            pygame.draw.rect(screen, color, 
                           (col*SQUARE_SIZE, row*SQUARE_SIZE,
                            SQUARE_SIZE, SQUARE_SIZE))
