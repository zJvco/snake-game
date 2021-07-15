import pygame
import sys
import os
from pygame import mixer
from snake import Snake
from apple import Apple

pygame.init()

WINDOW_SIZE = (600, 600)
WINDOW = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
FPS = 10

background_block_size = 15

score = 0
game_over = False

snake = Snake(background_block_size, WINDOW_SIZE)
apple = Apple(background_block_size)

eat_sound = mixer.Sound(os.path.join("assets/sounds", "eat_apple_sound.wav"))
game_over_sound = mixer.Sound(os.path.join("assets/sounds", "game_over_sound.wav"))


def check_collision(obj_1, obj_2):
    if obj_1.colliderect(obj_2):
        return True


def generate_background(window_size, bg_size):
    for y in range(int(window_size[1] / bg_size)):
        for x in range(int(window_size[0] / bg_size)):
            pygame.draw.rect(WINDOW, (150, 150, 150), (x * bg_size, y * bg_size, bg_size, bg_size), 1)


while True:
    WINDOW.fill((0, 0, 0))
    pygame.display.set_caption(f"Snake Game - Score: {score}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.vel_x >= 0:
                snake.vel_x = snake.speed
                snake.vel_y = 0
            if event.key == pygame.K_LEFT and snake.vel_x <= 0:
                snake.vel_x = -snake.speed
                snake.vel_y = 0
            if event.key == pygame.K_DOWN and snake.vel_y >= 0:
                snake.vel_y = snake.speed
                snake.vel_x = 0
            if event.key == pygame.K_UP and snake.vel_y <= 0:
                snake.vel_y = -snake.speed
                snake.vel_x = 0

    for i in range(len(snake.rect)):
        if i > 0 and check_collision(snake.rect[0], snake.rect[i]):
            game_over = True

    if game_over:
        game_over_sound.play()
        del snake.rect[1:]
        FPS = 10
        snake.rect[0].x, snake.rect[0].y = WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2
        snake.vel_x, snake.vel_y = 0, 0
        score = 0
        game_over = False

    if check_collision(snake.rect[0], apple.rect):
        eat_sound.play()
        apple.rect.x, apple.rect.y = apple.random_apple()[0], apple.random_apple()[1]
        snake.rect.append(pygame.Rect(snake.rect[0].x, snake.rect[0].y, snake.size, snake.size))
        score += 1
        FPS += 1
        if FPS > 30:
            FPS = 30

    apple.update(WINDOW)
    snake.update(WINDOW, WINDOW_SIZE)

    generate_background(WINDOW_SIZE, background_block_size)

    pygame.display.flip()
    clock.tick(FPS)