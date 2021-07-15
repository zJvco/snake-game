import pygame

class Snake:
    def __init__(self, bg_size, window_size):
        self.size = bg_size
        self.rect = [pygame.Rect(window_size[0]/2, window_size[1]/2, self.size, self.size)]
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 15

    def tail_position(self):
        for i in range(len(self.rect) - 1, 0, -1):
            self.rect[i].x = self.rect[i-1].x
            self.rect[i].y = self.rect[i-1].y

    def move(self, window_size):
        self.rect[0].x += self.vel_x
        self.rect[0].y += self.vel_y
        self.wall_collision(window_size)

    def wall_collision(self, window_size):
        if self.rect[0].x < 0:
            self.rect[0].x = window_size[0] - self.size
        if self.rect[0].x > window_size[0] - self.size:
            self.rect[0].x = 0
        if self.rect[0].y < 0:
            self.rect[0].y = window_size[1] - self.size
        if self.rect[0].y > window_size[1] - self.size:
            self.rect[0].y = 0

    def draw(self, window):
        for tail in self.rect:
            pygame.draw.rect(window, (0, 255, 0), tail)

    def update(self, window, window_size):
        self.tail_position()
        self.move(window_size)
        self.draw(window)
