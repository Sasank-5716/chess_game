from .piece import Piece

class Pawn(Piece):
    def get_legal_moves(self, board):
        moves = []
        row, col = self.pos
        direction = -1 if self.color == WHITE else 1
        
        # Single move
        if 0 <= row+direction < 8 and not board[row+direction][col]:
            moves.append((row+direction, col))
            
        # Double move
        if not self.has_moved and not board[row+2*direction][col] and not board[row+direction][col]:
            moves.append((row+2*direction, col))
            
        # Captures
        for dc in [-1, 1]:
            if 0 <= col+dc < 8 and 0 <= row+direction < 8:
                target = board[row+direction][col+dc]
                if target and target.color != self.color:
                    moves.append((row+direction, col+dc))
                    
        return moves
