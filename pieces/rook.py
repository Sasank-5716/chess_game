from .piece import Piece

class Rook(Piece):
    def get_legal_moves(self, board):
        moves = []
        row, col = self.pos
        
        # Horizontal
        for dc in [-1, 1]:
            c = col + dc
            while 0 <= c < 8:
                target = board[row][c]
                if not target:
                    moves.append((row, c))
                else:
                    if target.color != self.color:
                        moves.append((row, c))
                    break
                c += dc
                
        # Vertical
        for dr in [-1, 1]:
            r = row + dr
            while 0 <= r < 8:
                target = board[r][col]
                if not target:
                    moves.append((r, col))
                else:
                    if target.color != self.color:
                        moves.append((r, col))
                    break
                r += dr
                
        return moves
