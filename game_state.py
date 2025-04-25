from board import create_start_board
from constants import WHITE, BLACK
from pieces import King, Queen, Rook, Bishop, Knight, Pawn

class GameState:
    def __init__(self):
        self.board = create_start_board()
        self.turn = WHITE
        self.selected = None
        self.hover = None
        self.move_history = []
        self.checkmate = False
        self.stalemate = False
    
    def make_move(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        piece = self.board[start_row][start_col]
        captured = self.board[end_row][end_col]

    def in_check(self):
        king_pos = None
        # Find king
        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]
                if isinstance(piece, King) and piece.color == self.turn:
                    king_pos = (r,c)
                    break
            if king_pos: break
        
        # Check if any opponent piece attacks king
        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]
                if piece and piece.color != self.turn:
                    if piece.attacks(self.board, king_pos):
                        return True
        return False
    
    def get_all_legal_moves(self, color):
        moves = []
        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]
                if piece and piece.color == color:
                    for move in piece.get_legal_moves(self.board):
                        moves.append(((r,c), move))
        return moves
    
    def check_game_over(self):
        moves = self.get_all_legal_moves(self.turn)
        if not moves:
            if self.in_check():
                self.checkmate = True
            else:
                self.stalemate = True
