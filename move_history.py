def record_move(move, capture, checkmate=False):
    start, end = move
    piece = type(move[0]).__name__
    return f"{piece} {chr(ord('a')+start[1])}{8-start[0]}->{chr(ord('a')+end[1])}{8-end[0]}"

def draw_history(screen, history):
    font = pygame.font.SysFont('courier', 18)
    y = 20
    for i in range(0, len(history), 2):
        white = history[i]
        black = history[i+1] if i+1 < len(history) else ''
        text = f"{i//2+1}. {white}  {black}"
        txt_surf = font.render(text, True, (0,0,0))
        screen.blit(txt_surf, (WINDOW_SIZE+10, y))
        y += 25
