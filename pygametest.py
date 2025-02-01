from os import pipe
import pygame
from pygame.locals import *
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# initialize pygame
pygame.init()
screen_size = (700, 500)

# create a window
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("pygame Test")

# clock is used to set a max fps
clock = pygame.time.Clock()

# create a demo surface, and draw a red line diagonally across it

#surface_size = (25, 45)
#test_surface = pygame.Surface(surface_size)
#test_surface.fill(WHITE)
#pygame.draw.aaline(test_surface, RED, (0, surface_size[1]), (surface_size[0], 0))

player_rect = pygame.Rect(64,64,64,64)
pipe1 = pygame.Rect(700,200,100,300)
pipe2 = pygame.Rect(700,-200,100,300)
bird_pic = pygame.image.load('bird.png')
pipe_pic = pygame.image.load('pipe.png')
bird_pic = pygame.transform.scale(bird_pic, (64,64))
pipe_pic = pygame.transform.scale(pipe_pic, (100,300))
pipe_pic2 = pygame.transform.flip(pipe_pic, False, True)
running = True
moving_up = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                moving_up = True
        if event.type == pygame.KEYUP:
            if event.key == K_UP:
                moving_up = False


    if moving_up:
        player_rect.y-=15
    else:
        player_rect.y+=4
    #clear the screen
    screen.fill(WHITE)

    # draw to the screen
    # YOUR CODE HERE
    #x = (screen_size[0]/2) - (surface_size[0]/2)
    #y = (screen_size[1]/2) - (surface_size[1]/2)
    #screen.blit(test_surface, (x, y))
    #screen.blit(bird_pic, player_rect)

    pipe1.x-=2
    pipe2.x-=2
    screen.blit(pipe_pic2, pipe2)
    screen.blit(pipe_pic, pipe1)
    screen.blit(bird_pic, player_rect)
    #screen.blit(pipe_pic, player_rect)
    # flip() updates the screen to make our changes visible
    pygame.display.flip()

    # how many updates per second
    clock.tick(60)
    if player_rect.y>436:
        pygame.quit()
        
    
        



pygame.quit()