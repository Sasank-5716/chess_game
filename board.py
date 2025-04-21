# board.py
def draw_board(screen):
    colors = [(235,235,208), (119,149,86)]
    for row in range(8):
        for col in range(8):
            pygame.draw.rect(screen, colors[(row+col)%2],
                           (col*100, row*100, 100, 100))
