import pygame
from random import randint

class Apple:
    def __init__(self, bg_size):
        self.size = bg_size
        self.rect = pygame.Rect(self.random_apple()[0], self.random_apple()[1], self.size, self.size)

    @staticmethod
    def random_apple():
        while True:
            apple_random_x = randint(0, 580)
            apple_random_y = randint(0, 580)
            if apple_random_x % 15 == 0 and apple_random_y % 15 == 0:
                break
        return apple_random_x, apple_random_y

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), self.rect)

    def update(self, window):
        self.draw(window)