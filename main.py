import pygame
from game import ChessGame

def main():
    pygame.init()
    game = ChessGame()
    game.run()

if __name__ == "__main__":
    main()
