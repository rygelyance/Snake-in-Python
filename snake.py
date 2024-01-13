# Author: Rygel Yance
# Date: 01/12/2024
# This code is my first python project, which is a simple game of snake! Thought it would be great project to learn the basics of python and it'd be funny, being snake in Python. This project mainly relies on the pygame package to handle all of the graphics and input.

import pygame
import time
import random

pygame.init()
 
# Initializes a square window
window = pygame.display.set_mode((720, 720))
pygame.display.set_caption('Snake by Rygel Yance')
delta_time = 0
 
# Booleans to handle the loops for both gameplay and the window itself
running = True
game_over = False

# These global variables handle the score, the previous key pressed, and the speed of the snake
score = 0
prev_key = 0
snake_speed = 3
 
x = window.get_width() / 2
y = window.get_width() / 2
# This list represents each "block" of the snake using a list of coordinates, with x and y being in pixels
snake_arr = [[x, y]]

# Gets a random starting position for the food
food_x = random.randrange(18)*40
food_y = random.randrange(18)*40

# Represents how far the snake should move in the x and y directions respectively
x_change = 0       
y_change = 0
 
clock = pygame.time.Clock()

# Functions to handle the displaying of the messages shown after the end of a game
def game_over_msg(msg, color):
    mesg = pygame.font.SysFont(None, 70).render(msg, True, color)
    window.blit(mesg, [115, 310])

def try_again_msg(msg, color):
    mesg = pygame.font.SysFont(None, 70).render(msg, True, color)
    window.blit(mesg, [100, 410])

# Main window loop 
while running:
    # Main gameplay loop
    while not game_over:
        for event in pygame.event.get():
            # Quits the loop if the 'x' button on the window is pressed
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                 # Handles the input of the game using either wasd or the arrow keys. The prev_key variable is to make sure the snake cannot reverse direction.
                 if event.key == pygame.K_LEFT and prev_key != 1:
                     x_change = -40
                     y_change = 0
                 elif event.key == pygame.K_RIGHT and prev_key != 1:
                     x_change = 40
                     y_change = 0
                 elif event.key == pygame.K_UP and prev_key != 2:
                    y_change = -40
                    x_change = 0
                 elif event.key == pygame.K_DOWN and prev_key != 2:
                    y_change = 40
                    x_change = 0
                 elif event.key == pygame.K_a and prev_key != 1:
                     x_change = -40
                     y_change = 0
                 elif event.key == pygame.K_d and prev_key != 1:
                     x_change = 40
                     y_change = 0
                 elif event.key == pygame.K_w and prev_key != 2:
                    y_change = -40
                    x_change = 0
                 elif event.key == pygame.K_s and prev_key != 2:
                    y_change = 40
                    x_change = 0
 
        x += x_change
        y += y_change

        # Appends the latest coordinate to the snake list
        snake_arr.append([x, y])

        # Checks if the food is eaten or if the food spawns in the snake
        if x == food_x and y == food_y or [food_x, food_y] in snake_arr:
            score += 1
            # Increases the speed of the snake after every 10 points
            if score % 10 == 0:
                snake_speed += 1
            # Generates new random location for the next food item
            food_x = random.randrange(18)*40
            food_y = random.randrange(18)*40
        else:
            # Removes the first element of the snake list which is the oldest coordinate, or the tail of the snake. If food is eaten the tail will not be removed, thus the snake grows by one.
            snake_arr.pop(0)

        # Ends the game if the snake hits the edge of the window
        if x > 680 or x < 0 or y > 680 or y < 0:
            game_over = True
        # Ends the game if the snake hits itself
        if snake_arr.index([x, y]) != score:
                game_over = True

        # Sets the background color of the window
        window.fill('black')   
        # Draws the food in the window
        pygame.draw.circle(window, (222, 42, 66, 255), [food_x + 20, food_y + 20], 17)

        # Draws each segment of the snake then updates the window accordingly
        for coord in snake_arr:
            pygame.draw.rect(window, (120, 180, 84, 255), [coord[0], coord[1], 40, 40], 0, 10)
            pygame.draw.rect(window, (110, 170, 74, 255), [coord[0], coord[1], 40, 40], 3, 10)

        pygame.display.update()

        if x_change != 0:
            pygame.draw.circle(window, 'black', [x + 20, y + 9], 3)
            pygame.draw.circle(window, 'black', [x + 20, y + 31], 3)
            pygame.display.update()
            prev_key = 1
        elif y_change != 0:
            pygame.draw.circle(window, 'black', [x + 9, y + 20], 3)
            pygame.draw.circle(window, 'black', [x + 31, y + 20], 3)
            pygame.display.update()
            prev_key = 2

        # Sets the speed that the game runs at and allows the inputs to sync to the frame rate
        clock.tick(snake_speed)
    
    # Displays the game over messages and the option to try again
    game_over_msg('Game over! Score: {}'.format(score), 'white')
    try_again_msg('Try again? press Y or N', 'white')
    pygame.display.update()

    # Handles the options for quitting or restarting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # If the user chooses to play again, resets all of the key variables and the snake
            if event.key == pygame.K_y:
                score = 0
                prev_key = 0
                snake_speed = 3
                x = window.get_width() / 2
                y = window.get_width() / 2
                snake_arr = [[x, y]]
                food_x = random.randrange(18)*40
                food_y = random.randrange(18)*40
                x_change = 0       
                y_change = 0
                game_over = False
            elif event.key == pygame.K_n:
                running = False

pygame.quit()