import pickle

def save_game(game_state, filename='chess_save.pkl'):
    with open(filename, 'wb') as f:
        pickle.dump({
            'board': game_state.board,
            'turn': game_state.turn,
            'history': game_state.move_history
        }, f)

def load_game(filename='chess_save.pkl'):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    
    game_state = GameState()
    game_state.board = data['board']
    game_state.turn = data['turn']
    game_state.move_history = data['history']
    return game_state
