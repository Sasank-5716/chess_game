class Piece:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col
        self.moved = False
        
    def get_valid_moves(self, board):
        raise NotImplementedError
        
    def move(self, row, col):
        self.row = row
        self.col = col
        self.moved = True
