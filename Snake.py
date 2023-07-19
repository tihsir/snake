import pygame as pygame
import time
import random
pygame.init()
dis = pygame.display.set_mode((500, 500))
pygame.display.update()
pygame.display.set_caption("Snake Game")
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)


font_style = pygame.font.SysFont(None, 35)
clock = pygame.time.Clock()
def game():
    x = 250
    y = 250
    x_delta = 0
    y_delta = 0
    snake = []
    snake_length = 1
    food_x = round(random.randrange(0, 490) / 10.0) * 10.0
    food_y = round(random.randrange(0, 490) / 10.0) * 10.0
    game_finished = False
    game_close = False
    while not game_finished:
        while game_close:
            dis.fill((0,0,0))
            dis.blit(font_style.render("You Lose, Play Again? 'Y'-Yes, 'N'-No", True, red), [10, 200])
            pygame.display.update()
            for event in pygame.event.get():
                if event.key == pygame.K_n:
                    game_finished = True
                    game_close = False
                if event.key == pygame.K_y:
                    game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_ongoing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_delta = -10
                    y_delta = 0
                elif event.key == pygame.K_RIGHT:
                    x_delta = 10
                    y_delta = 0
                elif event.key == pygame.K_DOWN:
                    x_delta = 0
                    y_delta = 10
                elif event.key == pygame.K_UP:
                    x_delta = 0
                    y_delta = -10

        if (x > 500) or (y > 500) or (x < 0) or (y < 0):
            game_close = True

        x += x_delta
        y += y_delta
        dis.fill((0,0,0))
        dis.blit(font_style.render("Score: " + str(snake_length - 1), True, red), [0,0])
        pygame.draw.rect(dis, green, [food_x,food_y, 10, 10])
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake.append(snake_head)
        if len(snake) > snake_length:
            del snake[0]

        for i in snake[:-1]:
            if i == snake_head:
                game_close = True

        for i in snake:
            pygame.draw.rect(dis, red, [i[0],i[1], 10, 10])

        pygame.display.update()

        if (x == food_x) and (y == food_y):
            food_x = round(random.randrange(0, 490) / 10.0) * 10.0
            food_y = round(random.randrange(0, 490) / 10.0) * 10.0
            snake_length += 1
        pygame.display.update()
        clock.tick(5)
    pygame.quit()
    quit()

game()