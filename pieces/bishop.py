from .piece import Piece

class Bishop(Piece):
    def get_legal_moves(self, board):
        moves = []
        row, col = self.pos
        directions = [(-1,-1), (-1,1), (1,-1), (1,1)]
        
        for dr, dc in directions:
            r, c = row+dr, col+dc
            while 0 <= r < 8 and 0 <= c < 8:
                target = board[r][c]
                if not target:
                    moves.append((r, c))
                else:
                    if target.color != self.color:
                        moves.append((r, c))
                    break
                r += dr
                c += dc
                
        return moves
