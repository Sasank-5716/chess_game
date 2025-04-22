from .piece import Piece

class Knight(Piece):
    def get_legal_moves(self, board):
        moves = []
        row, col = self.pos
        offsets = [
            (2,1), (2,-1),
            (-2,1), (-2,-1),
            (1,2), (1,-2),
            (-1,2), (-1,-2)
        ]
        
        for dr, dc in offsets:
            r, c = row+dr, col+dc
            if 0 <= r < 8 and 0 <= c < 8:
                target = board[r][c]
                if not target or target.color != self.color:
                    moves.append((r, c))
                    
        return moves
