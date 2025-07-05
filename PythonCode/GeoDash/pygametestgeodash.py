"""
If you want to run locally:
1) 3 dots on top left, click Download as zip
2) Right click zip file in File Explorer, Extract All
3) Shift Right Click in folder you extracted in, and open in powershell
4) Do the usual with python 3



"""

import pygame
from pygame.locals import *
spawned = False
angle = 0
rotateframes = 0
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
CYAN = (0, 145, 165)
screen_size = (700, 500)
map = []
speed = []
mode = []
modeswap = False    
speed_rect = []
scroll_x = -screen_size[0] / 2
file = open("nnn.txt", "r")
txt = file.readlines()
y = 0
get_stats = True
map_num = -1
for line in txt:
  line = line.strip()
  # CHANGE
  if len(line) == 1 and line.isdigit():
    y = 0
    map.append([])
    get_stats = False
    map_num += 1
    continue
  if get_stats == False:
    stats = line.split (",")
    print (stats)
    speed.append (float(stats[0]))
    mode.append (stats[1])
    get_stats = True
  x = 0
  y += 1
  print(speed)
  print ("")
  # CHANGE
  map[map_num].append([])
  for tile in line:
    map[map_num][-1].append(tile)
    x += 1
print (map[0])

player_rect = pygame.Rect(100, -250, 32, 32)
player_surf = pygame.Surface((32, 32))
player_mask = pygame.mask.from_surface(player_surf)

# initialize pygame
pygame.init()
# create a window
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("pygame Test")

# clock is used to set a max fps
clock = pygame.time.Clock()
player_vy = 0
change_speed = 0
schanged = False
player_vx = 0 
running = True
respawn_point_x, respawn_point_y = [0, 0]
cur_level = 0

collisions = {"bottom" : False, "top" : False, "right" : False , "left" : False}

gravity = 0
spike_image = pygame.image.load('Spike.png').convert_alpha()
spikeflip_image = pygame.image.load('Spikeflip.png').convert_alpha()
geochar_image = pygame.image.load('Geochar.png')
spike_masks = []
moving_up = False
while running:
    scroll_x += player_rect.x - scroll_x - screen_size[0] / 2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                moving_up = True
                #player_vy = -6
                #rotateframes = 9
        if event.type == pygame.KEYUP:
            if event.key == K_UP:
                moving_up = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                moving_up = True
                #player_vy = -6
                #rotateframes = 9
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                moving_up = False

    collisionrects = []
    if mode[cur_level] == "jump" and collisions['bottom'] == True and moving_up == True: 
        player_vy = -6 
        rotateframes = 9
    if mode[cur_level] == "fly" and moving_up == True:
        player_vy = -4
    if mode[cur_level] == "fly" and moving_up == False:
        player_vy = 4
    if rotateframes > 0:
        rotateframes -= 1
        angle -= 10


    spikerects = []
    spike_masks = []        
    win_rect = []  
    mode_rect = []        
    player_vx = speed[cur_level]

    if mode[cur_level] == "jump":
        if gravity < 2:
            gravity += 0.02
        player_vy+=gravity


    #clear the screen
    screen.fill(BLACK)

    for y in range(len(map[cur_level])):
        # CHANGE
        currow = map[cur_level][y]
        for x in range(len(currow)):
            if currow[x] == '#':
               collisionrects.append(pygame.Rect(x * 32, y * 32, 32, 32))
               pygame.draw.rect(screen, WHITE, (x * 32 - scroll_x, y * 32, 32, 32))
            if currow[x] == '!':
               collisionrects.append(pygame.Rect(x * 32, y * 32, 32, 32))
               pygame.draw.rect(screen, BLACK, (x * 32 - scroll_x, y * 32, 32, 32))
            if currow[x] == '^':
               spikerects.append(pygame.Rect(x * 32, y * 32, 32, 32))
               # MASKS
               spike_masks.append(pygame.mask.from_surface(spike_image))
               screen.blit(spike_image, (x * 32 - scroll_x, y * 32, 32, 32))
            if currow[x] == '*':
               spikerects.append(pygame.Rect(x * 32, y * 32, 32, 32))
               # MASKS
               spike_masks.append(pygame.mask.from_surface(spikeflip_image))
               screen.blit(spikeflip_image, (x * 32 - scroll_x, y * 32, 32, 32))
            if currow[x] == 's' and spawned == False:               
               if cur_level == 0:
                    respawn_point_x = x * 32
                    respawn_point_y = y * 32


               player_rect.x = x * 32
               player_rect.y = y * 32 
               spawned = True
            if currow[x] == 'w':
               win_rect.append(pygame.Rect(x * 32, y * 32, 32, 32))
               pygame.draw.rect(screen, GREEN, (x * 32 - scroll_x, y * 32, 32, 32))
            if currow[x] == '/':
               mode_rect.append(pygame.Rect(x * 32, y * 32, 32, 32))
               pygame.draw.rect(screen, BLACK, (x * 32 - scroll_x, y * 32, 32, 32))

            if currow[x] in ["z"]:
               speed_rect.append([pygame.Rect(x * 32, y * 32, 32, 32),15])
               pygame.draw.rect(screen, CYAN, (x * 32 - scroll_x, y * 32, 32, 32))
            if currow[x] in ["n"]:
               speed_rect.append([pygame.Rect(x * 32, y * 32, 32, 32),20])
               pygame.draw.rect(screen, CYAN, (x * 32 - scroll_x, y * 32, 32, 32))
            if currow[x] in ["v"]:
               speed_rect.append([pygame.Rect(x * 32, y * 32, 32, 32),17])
               pygame.draw.rect(screen, CYAN, (x * 32 - scroll_x, y * 32, 32, 32))
            if currow[x] in ["x"]:
               speed_rect.append([pygame.Rect(x * 32, y * 32, 32, 32),10])
               pygame.draw.rect(screen, CYAN, (x * 32 - scroll_x, y * 32, 32, 32))
            if currow[x] in ["c"]:
               speed_rect.append([pygame.Rect(x * 32, y * 32, 32, 32),8])  
               pygame.draw.rect(screen, CYAN, (x * 32 - scroll_x, y * 32, 32, 32)) 
            if currow[x] in ["b"]:        
               speed_rect.append([pygame.Rect(x * 32, y * 32, 32, 32),4.5])
               pygame.draw.rect(screen, CYAN, (x * 32 - scroll_x, y * 32, 32, 32))



    rotated_player = pygame.transform.rotate(geochar_image, angle)
    screen.blit (rotated_player, (player_rect.x - scroll_x, player_rect.y))

    player_rect.y += player_vy


    for tile in win_rect:
        if player_rect.colliderect(tile):
            spawned = False
            modeswap = False
            player_rect.x = 0
            player_rect.y = 0
            # CHANGED
            cur_level += 1
            continue
    collisions = {"bottom" : False, "top" : False, "right" : False , "left" : False}
    for tile in collisionrects:
        if player_rect.colliderect(tile):
            if player_vy > 0:
               player_rect.bottom = tile.top 
               gravity = 0
               collisions["bottom"] = True
            if player_vy < 0: 
               player_rect.top = tile.bottom 
               gravity = 0
               collisions["top"] = True
    for tile in mode_rect:
        if player_rect.colliderect(tile) and modeswap == False:
            print ("true")
            if mode[cur_level] == "jump":
                mode[cur_level] = "fly"
            else:
                mode[cur_level] = "jump"
            modeswap = True
    for tile in speed_rect:
        if player_rect.colliderect(tile[0]):
            schanged = True
            change_speed = tile[1]

    if schanged == True:
        player_rect.x += change_speed
    else:
        player_rect.x += player_vx

    for tile in collisionrects:
        if player_rect.colliderect(tile):
            if player_vy > 0:
               player_rect.right = tile.left 
               gravity = 0
               collisions["right"] = True
               cur_level = 0
               player_rect.x = respawn_point_x
               player_rect.y = respawn_point_y        
               schanged = False
            if player_vy < 0: 
               player_rect.left = tile.right 
               collisions["left"] = True
               cur_level = 0
               player_rect.x = respawn_point_x
               player_rect.y = respawn_point_y
               schanged = False
    spike_count = 0
    for spike in spikerects:
        if player_rect.colliderect(spike):
            # MASK
            offset = (spike.x - player_rect.x, spike.y - player_rect.y)
            if player_mask.overlap(spike_masks[spike_count], offset):
               cur_level = 0
               player_rect.x = respawn_point_x
               player_rect.y = respawn_point_y
               schanged = False

        spike_count += 1



    # flip() updates the screen to make our changes visible
    pygame.display.flip()

    # how many updates per second
    clock.tick(60)





pygame.quit()
