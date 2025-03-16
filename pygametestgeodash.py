import pygame
from pygame.locals import *
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)



player_rect = pygame.Rect(100, -300, 50, 50)
sigma_rect = pygame.Rect(200, 150, 100000, 200)
# initialize pygame
pygame.init()
screen_size = (700, 500)
# create a window
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("pygame Test")

# clock is used to set a max fps
clock = pygame.time.Clock()
player_vy = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                moving_up = True
                player_vy = -20
        if event.type == pygame.KEYUP:
            if event.key == K_UP:
                moving_up = False




    
    player_vy+=1
    player_rect.y += player_vy
    if player_rect.colliderect(sigma_rect):
        player_rect.y = sigma_rect.top-player_rect.height
        player_vy = 0
    #clear the screen
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, player_rect)
    pygame.draw.rect(screen, WHITE, sigma_rect)
    sigma_rect.x-=2

    

    # flip() updates the screen to make our changes visible
    pygame.display.flip()

    # how many updates per second
    clock.tick(60)
    
pygame.quit()
