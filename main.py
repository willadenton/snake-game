'''
Best snake game ever
tutorial at: https://www.edureka.co/blog/snake-game-with-pygame/
'''

# import external libraries and code 
import pygame
import random
from grape import Snake
from colors import blue, white, red, green, purple 

# initialize pygame
pygame.init()

# setup the size of the game window 
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))

# draw the screen
pygame.display.update()

# set a caption on the screen
pygame.display.set_caption('Space Worm by Willa and Ev!')

# game clock: controls the speed of the game loop
clock = pygame.time.Clock()
snake_speed = 30 # higher number == faster snake == harder game
snake_color = purple
snake_head_size = 20

# create a snake
snake = Snake(purple, dis_width / 2, dis_height / 2)

# set up for messages to be displayed on the screen
font_style = pygame.font.SysFont(None, 50)

def display_score(score):
    """Draws the score for the game on the screen"""
    value = font_style.render("Your Score: " + str(score), True, blue)
    dis.blit(value, [10, 10])

def draw_snake(segment_size, snake_list):
    """Draws the segments of the snake"""
    for x in snake_list:
        pygame.draw.rect(dis, snake_color, [x[0], x[1], segment_size, segment_size])


def message(msg, color):
    """Displays a message `msg` in a `color` on the screen, anchored in the middle"""
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 2, dis_height / 2])


def game_loop():
    # create a variable to keep track of whether or not the game is over
    game_over = False
    game_close = False

    # variables to control the x/y coordinates and size of the snake head
    x1 = dis_width /2
    y1 = dis_height /2
    x1_change = 0
    y1_change = 0
    snake_list = []
    snake_length = 1
    snake_head_size = 10

    # get random x/y coordinated for the food
    foodx = (
        round(random.randrange(0, dis_width - snake_head_size) / snake_head_size) 
        * snake_head_size
    )
    foody = (
        round(random.randrange(0, dis_height - snake_head_size) / snake_head_size) 
        * snake_head_size
    )

    # the main game loop, this loop will run infinitely until the value
    # of 'game_over' changes from 'False' to 'True'
    while not game_over:
        while game_close == True:
            dis.fill(green)
            message("LMAO LOSER!! Press Q-Quit or C-Play Again!", red)
            pygame.display.update()
            # loops over all the events 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True 
            # if someone clicks a key on the keyboard
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_head_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:   
                    x1_change = snake_head_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_head_size
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_head_size

        # set 'game_close' to True if the snake goes outsife of the svreen boundaries
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(white)

        # draw a green rectangle to represent the food 
        pygame.draw.rect(dis, green, [foodx, foody, snake_head_size, snake_head_size])

     # establish the location of the snake's head
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        # makes sure we don't have an "phantom" or "extra" snake segments
        if len(snake.segments) > snake.length:
            del snake.segments[0]

        # check to see if the snake's head intersects with any of the snake body segments
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        snake.draw(dis)
        draw_snake(snake_head_size, snake_list)
        display_score(snake_length - 1)

        # update the surface (display area)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
             foodx = (
                round(
                    random.randrange(0, dis_width - snake_head_size) / snake_head_size
                )
                * snake_head_size
            )
             foody = (
                round(
                    random.randrange(0, dis_height - snake_head_size) / snake_head_size
                )
                * snake_head_size
            )
             snake_length += 1

        # sets clock speed; higher number == faster game (and more difficult!)
        clock.tick(snake_speed)

    # quit the game 
    pygame.quit()
    quit()

game_loop()