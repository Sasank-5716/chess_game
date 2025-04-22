from .piece import Piece
from .rook import Rook
from .bishop import Bishop

class Queen(Piece):
    def get_legal_moves(self, board):
        # Combine rook and bishop moves
        rook_moves = Rook(self.color, self.pos).get_legal_moves(board)
        bishop_moves = Bishop(self.color, self.pos).get_legal_moves(board)
        return rook_moves + bishop_moves
