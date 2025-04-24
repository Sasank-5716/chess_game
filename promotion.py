def show_promotion_menu(screen, color):
    pieces = [Queen, Rook, Bishop, Knight]
    rect = pygame.Rect(WINDOW_SIZE//2-100, WINDOW_SIZE//2-50, 200, 100)
    pygame.draw.rect(screen, (200,200,200), rect)
    
    for i, piece_type in enumerate(pieces):
        img = pygame.transform.scale(piece_images[color][piece_type], (40,40))
        screen.blit(img, (rect.x+10+i*50, rect.y+30))
    
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if rect.collidepoint(x,y):
                    index = (x - rect.x - 10) // 50
                    return pieces[index]
