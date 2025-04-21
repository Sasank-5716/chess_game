class Piece:
    def __init__(self, color, pos):
        self.color = color
        self.pos = pos
        self.image = None
        self.has_moved = False
        
    def get_legal_moves(self, board):
        raise NotImplementedError
        
    def attacks(self, board, pos):
        return pos in self.get_legal_moves(board)
    
