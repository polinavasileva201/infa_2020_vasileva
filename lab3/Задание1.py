import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

screen.fill((255,255,255))
#rect(screen, (255, 0, 255), (100, 100, 200, 200))
#rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)


polygon(screen, (0, 0, 0), [(166,158), (180,170),(190,158)])
circle(screen, (255, 255, 1), (200, 175), 80)
circle(screen, (0, 0, 0), (200, 175), 80, 1)

circle(screen, (254, 0, 0), (160, 150), 10)
circle(screen, (254, 0, 0), (240, 150), 15)

circle(screen, (0, 0, 0), (160, 150), 10,1)
circle(screen, (0, 0, 0), (240, 150), 15, 1)

circle(screen, (0, 0, 0), (160, 150), 5)
circle(screen, (0, 0, 0), (240, 150), 7)

polygon(screen, (0, 0, 0), [(160,200),(240,200),(240,210),(160,210)])


line(screen, (0,0,0), [125, 125], [180, 143], 8)
line(screen, (0,0,0), [285, 110], [215, 143], 8)





pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
