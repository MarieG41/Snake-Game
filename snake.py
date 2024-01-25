import pygame
import sys

pygame.init()

#width & height of the window for the Game
window_width = 800
window_height = 600
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Python Snake Game")

#Game loop
is_game_running = True

while is_game_running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_running = False

    #the snake
    snake_color = (64, 255, 166)
    snake_size = 20
    snake_x = window_width // 2
    snake_y = window_height // 2
    snake_speed = 5

    snake = pygame.Rect(snake_x, snake_y, snake_size, snake_size)

    #movements
    snake_dx = 0 
    snake_dy = 0

    #control
    snake_speed_multiplier = 1

    #update position
    snake_x += snake_dx * snake_speed * snake_speed_multiplier
    snake_y += snake_dy * snake_speed * snake_speed_multiplier

    #collision
    if snake.x < 0 or snake.x + snake_size > window_width or snake.y < 0 or snake.y + snake_size > window_height:
        is_game_running = False

    # Food properties
    import random
    food_color = (255, 0, 0)  # Red color
    food_size = 20

    # Place the food at a random position
    food_x = random.randint(0, window_width - food_size)
    food_y = random.randint(0, window_height - food_size)

    # Draw the food
    food = pygame.Rect(food_x, food_y, food_size, food_size)
    
    # Detect collisions between the snake and the food
    score = 0
    if snake.colliderect(food):
        # Update the snake's length and score
        snake_size += 1
        score += 1

        # Place the food at a new random position
        food.x = random.randint(0, window_width - food_size)
        food.y = random.randint(0, window_height - food_size)
        #n'affiche pas le serpent et les fruits
    pygame.display.update()

pygame.quit()
sys.exit()