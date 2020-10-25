import math
import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 50
sc = pygame.display.set_mode((1000, 600))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

time = 0

number_of_balls = 0

number_of_balls_2 = 0

circ_surf_list = []
circ_x_list = []
circ_y_list = []
circ_r_list = []

trian_surf_list = []
trian_x_list = []
trian_y_list = []
trian_a_list = []
trian_b_list = []
trian_phi_list = []
trian_dphi_list = []

circ_vx_list = []
circ_vy_list = []

#create new ball
def new_ball():
    global number_of_balls
    number_of_balls += 1
    
    x_ball = randint(100,600)
    y_ball = randint(100,600)
    r_ball = randint(30,50)
    vx_ball = randint(-15,15)
    vy_ball = randint(-15,15)

    
    #for ball movement 
    circ_surf = pygame.Surface((2 * r_ball, 2 * r_ball), pygame.SRCALPHA, 32)
    circ_surf = circ_surf.convert_alpha()
    circ_surf_list.append(circ_surf)
    
    circ_x_list.append(x_ball)
    circ_y_list.append(y_ball)
    circ_r_list.append(r_ball)

    circ_vx_list.append(vx_ball)
    circ_vy_list.append(vy_ball)
    
    color = COLORS[randint(0, 5)]
    circle(circ_surf, color, (r_ball, r_ball), r_ball)
    

#create new triangle
def new_ball_2():
    global number_of_balls_2
    number_of_balls_2 += 1
    
    x_ball_2 = randint(100,900)
    y_ball_2 = randint(100,500)
    a_ball_2 = randint(30,50)
    b_ball_2 = randint(60,90)
    dphi_ball_2 = randint(-10,10)
     
    
    trian_surf = pygame.Surface(( b_ball_2,  b_ball_2), pygame.SRCALPHA, 32)
    trian_surf = trian_surf.convert_alpha()
    trian_surf_list.append(trian_surf)
    

    trian_x_list.append(x_ball_2)
    trian_y_list.append(y_ball_2)
    trian_a_list.append(a_ball_2)
    trian_b_list.append(b_ball_2)
    trian_phi_list.append(0)
    trian_dphi_list.append(dphi_ball_2)
    
    color = COLORS[randint(0, 5)]
    polygon(trian_surf, color,((0,0),(0,b_ball_2),(a_ball_2,b_ball_2)))


#shows your results
points=0
def circle_click(x_ball, y_ball, r_ball, x0_ball, y0_ball):
    R=(x0_ball - x_ball)**2 + (y0_ball - y_ball)**2
    global points
    if R <= r_ball**2:
        points += 1
        print('Hit!')
        print('Points=', points)
        return True
    else:
        #print ('Beside!')
        return False

#shows your super results
points_super=0
def triangle_click(x_ball_2, y_ball_2, a_ball_2, b_ball_2, x0_ball, y0_ball):
    c_ball_2=math.sqrt((a_ball_2)**2+(b_ball_2)**2)
    R = c_ball_2/2
    #coordinates of the center of the circumscribed circle
    x1_ball_2 = (x_ball_2 + x_ball_2 + a_ball_2)/2
    y1_ball_2 = (y_ball_2 + y_ball_2 + b_ball_2)/2

    F = (x0_ball - x1_ball_2)**2 + (y0_ball - y1_ball_2)**2
    global points_super
    global points
    if F <= R**2:
        points_super+=1
        points+=3
        print('Hit_super!')
        print('Points_super=', points_super)
        print('Points=', points)
        return True
    else:
        return False


pygame.display.update()
clock = pygame.time.Clock()
finished = False


x_ball = y_ball = r_ball = 0
x_ball_2 = y_ball_2 = a_ball_2 = b_ball_2 = 0

while not finished:
    clock.tick(FPS)
    time += 1
    
    if(time % 12 == 0 and len(circ_surf_list) < 5):
        new_ball()

    if(time % 24 == 0 and len(circ_surf_list) < 5):
        new_ball()         
        
    if(time % 48 == 0 and len(trian_surf_list) < 5):
        new_ball_2()
     
    #ball movement 
    if(number_of_balls != 0):
        for circ_iter in range(len (circ_surf_list)):
            sc.blit(circ_surf_list[circ_iter],
                    (circ_x_list[circ_iter] - circ_r_list[circ_iter],
                     circ_y_list[circ_iter]- circ_r_list[circ_iter]))
            circ_x_list[circ_iter] += circ_vx_list[circ_iter]
            circ_y_list[circ_iter] += circ_vy_list[circ_iter]

             #reflection off the walls
            for i in range(len (circ_x_list)):
                if circ_x_list[i] < r_ball: 
                    circ_vx_list[circ_iter] *= -1
                    circ_x_list[circ_iter] = r_ball
                if circ_x_list[i] > 1000 - r_ball:
                    circ_vx_list[circ_iter] *= -1
                    circ_x_list[circ_iter] = 1000 - r_ball
            for i in range(len (circ_y_list)):
                if circ_y_list[i] < r_ball: 
                    circ_vy_list[circ_iter] *= -1
                    circ_y_list[circ_iter] = r_ball
                if circ_y_list[i] > 600 - r_ball:
                    circ_vy_list[circ_iter] *= -1
                    circ_y_list[circ_iter] = 600 - r_ball

                    
    #rotation of the triangle
    if(number_of_balls_2 != 0):
        for trian_iter in range(len(trian_surf_list)):
            trian_surf_2 = pygame.transform.rotate(trian_surf_list[trian_iter], 
                                                  trian_phi_list[trian_iter])
            trian_phi_list[trian_iter] += trian_dphi_list[trian_iter]
            sc.blit(trian_surf_2,
                    (trian_x_list[trian_iter], trian_y_list[trian_iter]))
              
    
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            finished = True
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            

            #return the coordinates of the place where we clicked with the mouse
            x0_ball, y0_ball = ev.pos
            
            range_balls = list(range(len (circ_surf_list)))
            for i in range_balls:
               x_ball = circ_x_list[i]
               y_ball = circ_y_list[i]
               r_ball = circ_r_list[i]
               if circle_click(x_ball, y_ball, r_ball, x0_ball, y0_ball):
                  circ_x_list.pop(i)
                  circ_y_list.pop(i)
                  circ_r_list.pop(i)
                  circ_surf_list.pop(i)

                  circ_vx_list.pop(i)
                  circ_vy_list.pop(i)
                  range_balls.pop()
            
            range_balls_2 = list(range(len (trian_surf_list)))
            for i in range_balls_2:
               x_ball_2 = trian_x_list[i]
               y_ball_2 = trian_y_list[i]
               a_ball_2 = trian_a_list[i]
               b_ball_2 = trian_b_list[i]
               if triangle_click(x_ball_2, y_ball_2, a_ball_2, b_ball_2,
                                 x0_ball, y0_ball):
                  trian_x_list.pop(i)
                  trian_y_list.pop(i)
                  trian_a_list.pop(i)
                  trian_b_list.pop(i)
                  trian_surf_list.pop(i)
                  range_balls_2.pop()     
      
                
    
    pygame.display.update()
    sc.fill(BLACK)

 
with open('best_result.txt', 'a') as file:
    if points_super >= 5 :
        #print('%Points= | %Points_surer=' % (points, points_super), file=file)      
        print('result of super player:',  file=file)
        print('Points=', points, '\n', 'Points_surer=', points_super, '\n',
                    '---------------', file=file)

pygame.quit()
















