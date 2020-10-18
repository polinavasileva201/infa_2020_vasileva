import math
import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
sc = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

time = 0

#create new ball
def new_ball():
    x_ball = randint(100,700)
    y_ball = randint(100,700)
    r_ball = randint(30,50)
    color = COLORS[randint(0, 5)]
    circle(sc, color, (x_ball, y_ball), r_ball)
    return x_ball, y_ball, r_ball

#create new triangle
def new_ball_2():
    x1 = randint(100,300)
    y1 = randint(100,400)
    x2 = randint(100,300)
    y2 = randint(100,400)
    x3 = randint(100,300)
    y3 = randint(100,400)
    
    color = COLORS[randint(0, 5)]
    polygon(sc, color, [(x1, y1), (x2, y2), (x3, y3)])
    return x1, y1, x2, y2, x3, y3 

#shows your results
points=0
def circle_click(x_ball, y_ball, r_ball, x0_ball, y0_ball):
    R=(x0_ball - x_ball)**2 + (y0_ball - y_ball)**2
    global points
    if R <= r_ball**2:
        points += 1
        print('Hit!')
        print('Points=', points)
    else:
        print ('Beside!')
        
pygame.display.update()
clock = pygame.time.Clock()
finished = False

#shows your super results
points_super=0
def triangle_click(x1, y1, x2, y2, x3, y3, x0, y0):
    #send lengths of a triangle
    a=math.sqrt((x2-x1)**2+(y2-y1)**2)
    b=math.sqrt((x3-x2)**2+(y3-y2)**2)
    c=math.sqrt((x1-x3)**2+(y1-y3)**2)
    if((a == 0) or (b == 0)):
        return

    #drawing up 
    x22=(x3+(c/a)*x2)/(1+(c/a))
    y22=(y3+(c/a)*y2)/(1+(c/a))
    x33=(x1+(a/b)*x3)/(1+(a/b))
    y33=(y1+(a/b)*y3)/(1+(a/b))

    k1=(y2-y33)/(x2-x33)
    b1=y2-k1*x2
    k2=(y1-y22)/(x1-x22)
    b2=y1-k2*x1

    x11=(b2-b1)/(k1-k2)
    y11=k1*x11+b1

    p=(a+b+c)/2
    S=math.sqrt(p*(p-a)*(p-b)*(p-c))
    f=S/p
    
    R=(x0 - x11)**2 + (y0 - y11)**2
    global points_super
    global points
    if R <= f**2:
        points_super+=1
        points+=3
        print('Hit_super!')
        print('Points_super=', points_super)
        print('Points=', points)

x_ball = y_ball = r_ball = 0
x1_tr = y1_tr = x2_tr = y2_tr = x3_tr = y3_tr = 0
while not finished:
    clock.tick(FPS)
    time += FPS
    
    if(time % 4 == 0):
        x_ball, y_ball, r_ball = new_ball()
        
    if(time % 8 == 0):
        x_ball, y_ball, r_ball = new_ball()

    if(time % 16 == 0):
        x_ball, y_ball, r_ball = new_ball()    
        
    if(time % 5 == 0):
        x1_tr, y1_tr, x2_tr, y2_tr, x3_tr, y3_tr = new_ball_2()

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            finished = True
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')

            #return the coordinates of the place where we clicked with the mouse
            x0_ball, y0_ball = ev.pos
            
            circle_click(x_ball, y_ball, r_ball, x0_ball, y0_ball)
            triangle_click(x1_tr, y1_tr, x2_tr, y2_tr, x3_tr, y3_tr, x0_ball, y0_ball)
    
    pygame.display.update()
    sc.fill(BLACK)

 
with open('best_result.txt', 'a') as file:
    if points_super >= 5 :
        #print('%Points= | %Points_surer=' % (points, points_super), file=file)      
        print('result of super player:',  file=file)
        print('Points=', points, '\n', 'Points_surer=', points_super, '\n',
                    '---------------', file=file)

pygame.quit()
















