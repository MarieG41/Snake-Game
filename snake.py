import pygame
import sys, random, time

pygame.init()

#width & height of the window for the Game
window_width = 800
window_height = 600
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Python Snake Game")
font = pygame.font.SysFont('comicsans',40)
game = True
clock = pygame.time.Clock()

#menu game
def main_menu():
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                main()

        game_window.fill((0,0,0))

        main_menu_msg = font.render('Press anywhere to start the game' , True, (255,255,255))
        font_position = main_menu_msg.get_rect(center=(window_width//2, window_height//2))
        game_window.blit(main_menu_msg , font_position)

        pygame.display.update()

#game over
def game_over(score):
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        game_window.fill((0,0,0))

        game_over_msg = font.render('You Lost' , True , (255,0,0))
        game_over_score = font.render(f'Your score was {score}' , True , (255,255,255))

        font_position_msg = game_over_msg.get_rect(center=(window_width//2, window_height//2))
        font_position_score = game_over_score.get_rect(center=(window_width//2, window_height//2+40))

        game_window.blit(game_over_msg , font_position_msg)
        game_window.blit(game_over_score , font_position_score)

        pygame.display.update()

        time.sleep(3)
        main_menu()

#Game loop
def main():
    snake_position = [200,70]
    snake_body = [[200,70] , [200-10,70] , [200-(2*10),70]]
    direction = 'right'
    score = 0
    fruit_spawn = True
    fruit_position = [0,0]
    clock = pygame.time.Clock()
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_UP]) and direction != 'down':
            direction = 'up'
        if (keys[pygame.K_DOWN]) and direction != 'up':
            direction = 'down'
        if(keys[pygame.K_RIGHT]) and direction != 'left':
            direction = 'right'
        if(keys[pygame.K_LEFT]) and direction != 'right':
            direction = 'left'

        game_window.fill((0,0,0))
        for square in snake_body:
            pygame.draw.rect(game_window, (255, 255, 0), (square[0], square[1],10,10))
        if direction == 'right':
            snake_position[0] += 10
        elif direction == 'left':
            snake_position[0] -= 10
        elif direction == 'up':
            snake_position[1] -= 10
        elif direction == 'down':
            snake_position[1] += 10
        
        snake_body.append(list(snake_position))

        if snake_position[0] <=0 or snake_position[0] >= window_width:
            game_over(score)
        if snake_position[1] <=0 or snake_position[1] >= window_height:
            game_over(score)
        
        if fruit_spawn:
            fruit_position = [random.randrange(40,window_width-40), random.randrange(40,window_height-40)]
            fruit_spawn = False
        pygame.draw.rect(game_window, (138,43,226),(fruit_position[0],fruit_position[1],10,10))

        score_font = font.render(f'{score}' , True , (255,255,255))
        font_position = score_font.get_rect(center=(window_width//2-40 , 30))
        game_window.blit(score_font , font_position)

        if pygame.Rect(snake_position[0],snake_position[1],10,10).colliderect(pygame.Rect(fruit_position[0],fruit_position[1],10,10)):
            fruit_spawn= True
            score += 5
        else:
            snake_body.pop(0)

        for square in snake_body[:-1]:
            if pygame.Rect(square[0],square[1],10,10).colliderect(pygame.Rect(snake_position[0],snake_position[1],10,10)):
                game_over(score)

        pygame.display.update()
        clock.tick(25) 
main_menu()   