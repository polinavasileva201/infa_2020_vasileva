import pygame
from pygame.draw import *
import numpy as np

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 400))

screen.fill((255,255,255))

polygon(screen, (0, 254, 255), [(0,0), (800,0),(800,170),(0,170)])
polygon(screen, (0, 220, 12), [(0,170), (800,170),(800,400),(0,400)])



def draw_sun(x,y,R,n):
    q=(np.pi)*(360/n)/180
    m1=[]
    m2=[]
    k=0
    while k<=9:
        P = []
        P.append(int(x + R*(np.cos(q/2 + k*q))))
                 
        P.append(int(y + R*(np.sin(q/2 + k*q))))
        T = []
        T.append(int(x + R*(np.cos(k*q))))
        T.append(int(y + R*(np.sin(k*q))))
        m1.append(P)
        m2.append(T)                                                    
        k+=1
    polygon(screen, (254,0,255), m1)
    polygon(screen, (0,0,0), m1, 1)
    
    polygon(screen, (254,0,255), m2)
    polygon(screen, (0,0,0), m2, 1)                                  
    
                                                     


def draw_house(w,h,x,y,w1,h1):

    polygon(screen, (255, 107, 0), [(x,y), (x+w,y),(x+w, y+h),(x,y+h)])
    polygon(screen, (0, 0, 0), [(x,y), (x+w,y),(x+w, y+h),(x,y+h)], 1)

    polygon(screen, (4, 220, 254), [ (int(x+(w-w1)/2),int(y+(h-h1)/2)),(int(x+(w-w1)/2+w1),int(y+(h-h1)/2)),
                                    (int(x+(w-w1)/2+w1),int(y+(h-h1)/2+h1)),(int(x+(w-w1)/2),int(y+(h-h1)/2+h1)) ] )

    polygon(screen, (255, 12, 0), [(x,y),(int(x+w/2),int(y-h/2)),(x+w,y)])
    polygon(screen, (0, 0, 0), [(x,y),(int(x+w/2),int(y-h/2)),(x+w,y)], 1)

#draw_house(200,130,100,120,60,50)



def draw_tree(x,y,w,h,x0,y0,R):
    polygon(screen, (0, 0, 0), [(x,y),(x+w,y),(x+w,y+h),(x,y+h)])
    circle(screen, (0, 145, 23), (x0, y0), R)
    circle(screen, (0, 0, 0), (x0, y0), R, 1)
    n=5
    q=(np.pi)*(360/n)/180
    k=0
    while k<=4:
            circle(screen, (0, 145, 23), (int(x0+R*(np.cos(k*q))), int(y0+R*(np.sin(q/2 + k*q)))), R)
            circle(screen, (0, 0, 0), (int(x0+R*(np.cos(k*q))), int(y0+R*(np.sin(q/2 + k*q)))), R, 1)
            k+=1


                   

def draw_clouds(x,y,R):
    k=0
    while k<=3:
            circle(screen, (255,250,250),(x + k*R , y), R)
            circle(screen, (0, 0, 0),(x + k*R , y), R, 1)
            k+=1
    circle(screen, (255,250,250),(x + R , y-R), R)
    circle(screen, (0, 0, 0),(x + R , y-R), R, 1)
    circle(screen, (255,250,250),(x + 2*R , y-R), R)
    circle(screen, (0, 0, 0),(x + 2*R , y-R), R, 1)

    
draw_sun(80,44,42,10)

draw_house(200,130,70,180,60,50)
draw_house(100,65,500,150,30,25)


draw_tree(380,185,16,110,388,155,25)
draw_tree(650,160,10,55,655,140,15)    

draw_clouds(160,70,30)
draw_clouds(600, 70, 35)
draw_clouds(400, 85, 20) 
       

    

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

