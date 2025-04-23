import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.move_sound = pygame.mixer.Sound('assets/move.wav')
        self.capture_sound = pygame.mixer.Sound('assets/capture.wav')
        self.check_sound = pygame.mixer.Sound('assets/check.wav')
        
    def play_move(self):
        self.move_sound.play()
        
    def play_capture(self):
        self.capture_sound.play()
        
    def play_check(self):
        self.check_sound.play()
