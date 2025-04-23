def is_valid_move(game_state, start, end):
    start_row, start_col = start
    end_row, end_col = end
    piece = game_state.board[start_row][start_col]
    
    if not piece:
        return False
        
    # Check if move is in piece's legal moves
    if (end_row, end_col) not in piece.get_legal_moves(game_state.board):
        return False
        
    # Simulate move
    temp = game_state.board[end_row][end_col]
    game_state.board[end_row][end_col] = piece
    game_state.board[start_row][start_col] = None
    
    # Check if move leaves king in check
    in_check = game_state.in_check()
    
    # Undo move
    game_state.board[start_row][start_col] = piece
    game_state.board[end_row][end_col] = temp
    
    return not in_check
