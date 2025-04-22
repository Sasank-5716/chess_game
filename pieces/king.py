from .piece import Piece

class King(Piece):
    def get_legal_moves(self, board):
        moves = []
        row, col = self.pos
        offsets = [
            (-1,-1), (-1,0), (-1,1),
            (0,-1),         (0,1),
            (1,-1),  (1,0), (1,1)
        ]
        
        for dr, dc in offsets:
            r, c = row+dr, col+dc
            if 0 <= r < 8 and 0 <= c < 8:
                target = board[r][c]
                if not target or target.color != self.color:
                    moves.append((r, c))
                    
        # Castling
        if not self.has_moved:
            # Queenside
            if board[row][0] and not board[row][0].has_moved:
                if all(board[row][c] is None for c in [1,2,3]):
                    moves.append((row, 2))
                    
            # Kingside
            if board[row][7] and not board[row][7].has_moved:
                if all(board[row][c] is None for c in [5,6]):
                    moves.append((row, 6))
                    
        return moves
