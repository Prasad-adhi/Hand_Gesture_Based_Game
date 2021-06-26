import pygame
import numpy as np
pygame.init()
screen = pygame.display.set_mode((400, 700))
clock = pygame.time.Clock()
done = False
grid=np.zeros([80,140],dtype=int)
grid[:,0]=100
grid[:,138]=-100
grid[0,:]=2
grid[78,:]=2
grid=np.transpose(grid)
grid[20,:]=-1
grid[120,10:22]=1
grid[40,70]=5
pug_x=np.where(grid==5)[1][0]
pug_y=np.where(grid==5)[0][0]
pug_top=False
pug_left=True
x=np.where(grid==1)[1][0]
y=np.where(grid==1)[0][0]
color = (255, 100, 0)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        #x -= 3
        if(grid[y][x-1]!=2):
            grid[120,x:x+12]=0
            x-=1
            grid[120,x:x+12]=1
            x=np.where(grid==1)[1][0]
            
    if pressed[pygame.K_RIGHT]: 
        #x += 3
        if(grid[y][x+12+1]!=2):
            grid[120,x:x+12]=0
            x+=1
            grid[120,x:x+12]=1
            x=np.where(grid==1)[1][0]
    if(pug_top):
        if(grid[pug_y-1,pug_x]==-1):
            pug_top=False
        else:
            grid[pug_y,pug_x]=0
            pug_y-=1
            grid[pug_y,pug_x]=5
    else:
        if(grid[pug_y+1,pug_x]==1):
            pug_top=True
        else:
            grid[pug_y,pug_x]=0
            pug_y+=1
            grid[pug_y,pug_x]=5
    if(pug_left):
        if(grid[pug_y,pug_x-1]==2):
            pug_left=False
        else:
            grid[pug_y,pug_x]=0
            pug_x-=1
            grid[pug_y,pug_x]=5
    else:
        if(grid[pug_y,pug_x+1]==2):
            pug_left=True
        else:
            grid[pug_y,pug_x]=0
            pug_x+=1
            grid[pug_y,pug_x]=5
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color, pygame.Rect(x*5, y*5, 60, 10))
    pygame.draw.rect(screen, (0,255,0), pygame.Rect(pug_x*5, pug_y*5, 10, 10))
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(0, 0, 400, 10))#top wall
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(0, 0, 10, 700))#left wall
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(0, 690, 400, 10))#bottom wall
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(390, 0, 10, 700))#right wall
    pygame.display.flip()
    clock.tick(60)