import random
from copy import deepcopy

class ChessAI:
    def __init__(self, color, difficulty=3):
        self.color = color
        self.difficulty = difficulty
        
    def evaluate_board(self, board):
        score = 0
        piece_values = {
            Pawn: 1, Knight: 3, Bishop: 3,
            Rook: 5, Queen: 9, King: 100
        }
        
        for row in board:
            for piece in row:
                if piece:
                    value = piece_values[type(piece)]
                    score += value if piece.color == self.color else -value
        return score

    def minimax(self, game_state, depth, alpha, beta, maximizing_player):
        if depth == 0 or game_state.checkmate or game_state.stalemate:
            return self.evaluate_board(game_state.board), None
            
        moves = game_state.get_all_legal_moves(
            self.color if maximizing_player else ('black' if self.color == 'white' else 'white')
        )
        
        best_move = None
        if maximizing_player:
            max_score = -float('inf')
            for move in moves:
                copy_state = deepcopy(game_state)
                copy_state.make_move(move[0], move[1])
                
                score, _ = self.minimax(copy_state, depth-1, alpha, beta, False)
                if score > max_score:
                    max_score = score
                    best_move = move
                
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
            return max_score, best_move
        else:
            min_score = float('inf')
            for move in moves:
                copy_state = deepcopy(game_state)
                copy_state.make_move(move[0], move[1])
                
                score, _ = self.minimax(copy_state, depth-1, alpha, beta, True)
                if score < min_score:
                    min_score = score
                    best_move = move
                
                beta = min(beta, score)
                if beta <= alpha:
                    break
            return min_score, best_move

    def get_best_move(self, game_state):
        _, move = self.minimax(game_state, self.difficulty, -float('inf'), float('inf'), True)
        return move

