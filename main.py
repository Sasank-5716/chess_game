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

def main():
    game_state = GameState()
    ai = ChessAI('black', difficulty=3)
    mode = 'pvp'  # or 'pvc'
    selected = None
    legal_moves = []
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
                
            # Handle input
            if mode == 'pvp' or game_state.turn == 'white':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    col = x // SQUARE_SIZE
                    row = y // SQUARE_SIZE
                    
                    if selected:
                        if (row,col) in legal_moves:
                            # Make move
                            game_state.make_move(selected, (row,col))
                            sound.play_move()
                            selected = None
                            legal_moves = []
                        else:
                            selected = None
                            legal_moves = []
                    else:
                        piece = game_state.board[row][col]
                        if piece and piece.color == game_state.turn:
                            selected = (row,col)
                            legal_moves = [m for m in piece.get_legal_moves(game_state.board) 
                                         if is_valid_move(game_state, selected, m)]
        
        # AI move
        if mode == 'pvc' and game_state.turn == 'black' and not game_state.checkmate:
            move = ai.get_best_move(game_state)
            if move:
                game_state.make_move(move[0], move[1])
                sound.play_move()

        screen.fill((0,0,0))
        draw_board(screen)
        if selected:
            draw_highlights(screen, legal_moves)
        draw_pieces(screen, game_state.board, piece_images)
        show_credits(screen)
        
        if game_state.checkmate:
            draw_game_over(screen)
        
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()