import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 200
FPS = 60

WHITE = (255, 255, 255)
GREEN = (34, 139, 34)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

dino_rect = pygame.Rect(50, 150, 40, 40)
velocity_y = 0
gravity = 1
is_jumping = False

cactus_rect = pygame.Rect(600, 160, 20, 30)
cactus_speed = 5
score = 0

font = pygame.font.SysFont("Arial", 24)

while True:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                velocity_y = -15
                is_jumping = True

    velocity_y += gravity
    dino_rect.y += velocity_y
    
    if dino_rect.bottom >= 190:
        dino_rect.bottom = 190
        is_jumping = False

    cactus_rect.x -= cactus_speed
    
    if cactus_rect.right < 0:
        cactus_rect.x = SCREEN_WIDTH + random.randint(0, 300)
        score += 1
        cactus_speed += 0.2
        
        cactus_rect.width = 20 * random.randint(1, 3)

    if dino_rect.colliderect(cactus_rect):
        pygame.quit()
        sys.exit()

    pygame.draw.line(screen, BLACK, (0, 190), (600, 190), 2)
    pygame.draw.rect(screen, GREEN, dino_rect)
    pygame.draw.rect(screen, RED, cactus_rect)
    
    score_surface = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_surface, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)