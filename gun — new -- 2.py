from random import randrange as rnd, choice
import random
import numpy as np
import pygame
from pygame.draw import *
from random import randint
import math
import time
pygame.init()

FPS = 50
sc = pygame.display.set_mode((800, 600))

BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (255,53,0)

BLACK = (0, 0, 0)
WHITE = (255,255,255)
ORANGE = (254,106,0)
COLORS = [BLUE, GREEN, ORANGE, BROWN]

sc.fill(WHITE)

time = 0

class Game_Object():
    def __init__(self, x, y, vx, vy, slow=1, g=0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.slow = slow
        self.g = g

        
        
    def update(self):
        pass
    
    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
    
        self.x += self.vx
        self.y -= self.vy
        self.vx +=0
        self.vy -= self.g

        if self.x < self.r: 
            self.vx *= - self.slow
            self.x = self.r
        if self.x > 800 - self.r:
            self.vx *= - self.slow
            self.x = 800 - self.r
        
        if self.y < self.r: 
            self.vy *= - self.slow
            self.y = self.r
        if self.y > 600 - self.r:
            self.vy *= - self.slow
            self.y = 600 - self.r

    def move_gun(self):
        self.x += self.vx
        #self.y -= self.vy
        #self.vx +=0
        #self.vy -= self.g

        if self.x < 20: 
            self.vx *= - self.slow
            self.x = 20
        if self.x > 780:
            self.vx *= - self.slow
            self.x = 780
        '''
        if self.y < self.r: 
            self.vy *= - self.slow
            self.y = self.r
        if self.y > 600 - self.r:
            self.vy *= - self.slow
            self.y = 600 - self.r        
        '''
    def hittest_gun(self, obj):
        
        if (obj.x - self.x)**2 + (obj.y - self.y)**2 <= (15 + self.r)**2:
            return True
        
        else:
            return False
    
class Targets():
    def __init__(self, x=0, y=0, vx=0, vy=0):
        self.points = 0
        self.live = 1
        
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = rnd(600, 750)
        self.y = rnd(300, 550)
        self.r = rnd(10, 50)
        self.vx = rnd(-10, 10)
        self.vy = rnd(-10, 10)
        
        
    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.id = ellipse( sc, color, ( -10, -10, -10, -10))
        self.points += points

        myfont = pygame.font.SysFont('Comic Sans MS', 28)
        self.id_points = myfont.render(self.points, False, (0, 0, 0)) 
        sc.blit(self.id_points,(30,30)) 


    
class Balls():
    def __init__(self, x=40, y=450, vx=0, vy=0):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.r = 10
       
        self.color = COLORS[randint(0, 3)]
        
        self.live = 30
        
    
    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (obj.x - self.x)**2 + (obj.y - self.y)**2 <= (obj.r + self.r)**2:
            return True
        
        else:
            return False

        
   
        '''
        id1 = circle( sc, self.color, (int(self.x), int(self.y)), self.r)
        id2 = rect( sc, self.color, (int(self.x), int(self.y), 2*self.r, 2*self.r))
        id3 = polygon( sc, self.color, ( (int(self.x), int(self.y)),(int(self.x)+2*self.r, int(self.y)), (int(self.x), int(self.y)-2*self.r) ) )
        id_list = [id1, id2, id3]
        self.id = random.choice(id_list)
        '''
        #self.id = random.choice([circle( sc, self.color, (int(self.x), int(self.y)), self.r),
        #                         rect( sc, self.color, (int(self.x), int(self.y), 2*self.r, 2*self.r)),
        #                         polygon( sc, self.color, ( (int(self.x), int(self.y)),(int(self.x)+2*self.r, int(self.y)), (int(self.x), int(self.y)-2*self.r) ) )])



class ball_1(Game_Object, Balls):
    def __init__(self, x=40, y=450, vx=0, vy=0):
        
        super().__init__(x, y, vx, vy, 0.85, 1)
        self.r = 10
       
        self.color = COLORS[randint(0, 3)]
        
        self.live = 30

        
    def update(self):
        self.id = circle( sc, self.color, (int(self.x), int(self.y)), self.r)

class ball_2(Game_Object, Balls):
    def __init__(self, x=40, y=450, vx=0, vy=0):
        
        super().__init__(x, y, vx, vy, 0.85, 1)
        self.r = 10
       
        self.color = COLORS[randint(0, 3)]
        
        self.live = 30

        
    def update(self):
        self.id = rect( sc, self.color, (int(self.x), int(self.y),
                                         2*self.r, 2*self.r))


class ball_3(Game_Object, Balls):
    def __init__(self, x=40, y=450, vx=0, vy=0):
        
        super().__init__(x, y, vx, vy, 0.85, 1)
        self.r = 10
       
        self.color = COLORS[randint(0, 3)]
        
        self.live = 30

        
    def update(self):
        self.id = polygon( sc, self.color, ( (int(self.x), int(self.y)),
                                        (int(self.x)+2*self.r, int(self.y)),
                                        (int(self.x), int(self.y)-2*self.r) ) )    





class gun():
    def __init__(self, x=20, y=450, vx=0, vy=0):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1

        #super().__init__(x, y, 1, vy)
        #super().__init__(x, y, vx, vy)
        
        self.color = BLACK
        
    def fire2_start(self, event):
        self.f2_on = 1
        self.color = ORANGE

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
         
        x = self.f2_power * math.cos(self.an) + self.x
        y = self.f2_power * math.sin(self.an) + self.y
        
        vx = self.f2_power * math.cos(self.an)
        vy = - self.f2_power * math.sin(self.an)


        new_ball = random.choice([ball_1(x, y, vx, vy),ball_2(x, y, vx, vy),
                                  ball_3(x, y, vx, vy)])
        '''
        new_ball_1 = ball_1(x, y, vx, vy)
        new_ball_1.r += 5
        new_ball_2 = ball_2(x, y, vx, vy)
        new_ball_2.r += 5
        new_ball_3 = ball_3(x, y, vx, vy)
        new_ball_3.r += 5
        
        balls += [new_ball_1]
        balls += [new_ball_2]
        balls += [new_ball_3]
        '''
        balls += [new_ball]

        '''   
        Balls += balls
        Balls += balls_2
        Balls += balls_3
        '''
    
        self.f2_on = 0
        self.f2_power = 10
        self.color = BLACK


            
    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event.pos[0] != self.x:
            self.an = math.atan((event.pos[1]-self.y) / (event.pos[0]-self.x))
        
        else:
            self.an = 1

        if(event.pos[0]-self.x < 0):
            self.an = np.pi + self.an     
    '''
    def update(self):   
         self.id = line(sc, self.color,(self.x,self.y),
                    (int(self.x + max(self.f2_power, 20) * math.cos(self.an)),
                    int(self.y + max(self.f2_power, 20) * math.sin(self.an))),7)

         self.id = circle(sc, BLACK, (self.x,self.y), 15, 2)  
     '''     
     
    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1


class gun_1(Game_Object, gun):
    def __init__(self, x=20, y=150, vx=0, vy=0):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        super().__init__(x, y, 1, vy)
        #super().__init__(x, y, vx, vy)
        self.color = BLACK
    def update(self):   
         self.id = line(sc, self.color,(self.x,self.y),
                    (int(self.x + max(self.f2_power, 20) * math.cos(self.an)),
                    int(self.y + max(self.f2_power, 20) * math.sin(self.an))),7)

         self.id = circle(sc, BLACK, (self.x,self.y), 15, 2)
         
class gun_2(Game_Object, gun):
    def __init__(self, x=20, y=400, vx=0, vy=0):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        super().__init__(x, y, 2, vy)
        #super().__init__(x, y, vx, vy)
        self.color = BLACK
    def update(self):   
         self.id = line(sc, self.color,(self.x,self.y),
                    (int(self.x + max(self.f2_power, 20) * math.cos(self.an)),
                    int(self.y + max(self.f2_power, 20) * math.sin(self.an))),7)

         self.id = circle(sc, BLACK, (self.x,self.y), 15, 2)      


class target_1(Game_Object, Targets):
    def __init__(self, x=0, y=0, vx=0, vy=0):
        self.points = 0
        self.live = 1
        
        super().__init__(x, y, vx, vy, 1, 0.1)
        
        self.new_target()

    def update(self):
        self.id = circle( sc, RED, (int(self.x), int(self.y)), self.r)

class target_2(Game_Object, Targets):
    def __init__(self, x=0, y=0, vx=0, vy=0):
        self.points = 0
        self.live = 1
        
        super().__init__(x, y, vx, vy)
        
        self.new_target()

    def update(self):
        self.id = rect( sc, RED, (int(self.x), int(self.y),
                                          2*self.r, 2*self.r))
        
class target_3(Game_Object, Targets):
    def __init__(self, x=0, y=0, vx=0, vy=0):
        self.points = 0
        self.live = 1
        
        super().__init__(x, y, vx, vy)
        
        self.new_target()

    def update(self):
        self.id = polygon( sc, RED, ( (int(self.x), int(self.y)),
                                          (int(self.x)+2*self.r, int(self.y)),
                                        (int(self.x), int(self.y)-2*self.r) ) )

class target_4(Game_Object, Targets):
    def __init__(self, x=0, y=0, vx=0, vy=0):
        self.points = 0
        self.live = 1
        
        super().__init__(x, y, vx, vy, 0.85, 0.3)
        
        self.new_target()

    def update(self):
        self.id = circle( sc, BLACK, (int(self.x), int(self.y)), self.r)




       
t1 = target_1()
t2 = target_2()
t3 = target_3()
t4 = target_4()

targets = []
targets += [t1]
targets += [t2]
targets += [t3]
targets += [t4]

targets_4 = []
targets_4 += [t4]

#g1 = gun()

g11 = gun_1()
g22 = gun_2()

guns = []
guns += [g11]
guns += [g22]


bullet = 0
balls = []
#Balls = []



pygame.display.update()
clock = pygame.time.Clock()
finished = False

gun, t1, balls, bullet, gun_1, gun_2


bullet = 0
balls = []
#Balls = []

    
while not finished:
    clock.tick(FPS)
    time += 1

    
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            finished = True
            
        if ev.type == pygame.MOUSEMOTION:
            #g1.targetting(ev)
            g11.targetting(ev)
            g22.targetting(ev)
            #for j in guns:
             #   j.targetting(ev)
            
        if ev.type == pygame.MOUSEBUTTONDOWN:
            #g1.fire2_start(ev)
            g11.fire2_start(ev)
            g22.fire2_start(ev)
            #for j in guns:
             #   j.fire2_start(ev)
        if ev.type == pygame.MOUSEBUTTONUP:
            #g1.fire2_end(ev)
            g11.fire2_end(ev)
            g22.fire2_end(ev)
            #for j in guns:
             #   j.fire2_end(ev)
            
    mousebutton = pygame.mouse.get_pressed()
    if mousebutton[0]:
        #g1.power_up()
        g11.power_up()
        g22.power_up()
        #for j in guns:
         #       j.power_up()

    #g1.move_gun()    
    #g1.update()
    '''    
    g11.move_gun()    
    g11.update()   
    g22.move_gun()    
    g22.update() 
    '''
    
    '''
    for num_g, j in enumerate(guns):
        for num, i in enumerate(targets_4):
            if num_g == 0:
                i.move()
                i.update()
            if i.hittest_gun(j):
                guns.pop(num_g)
                targets_4.pop(num)
                t_tmp = target_4()
                targets_4 += [t_tmp]         
    '''

    for num_g, j in enumerate(guns):
        g11.move_gun()    
        g11.update()   
        g22.move_gun()    
        g22.update()
        for num, i in enumerate(targets_4):
            if num_g == 0:
                i.move()
                i.update()
            if i.hittest_gun(j):
                guns.pop(num_g)
                targets_4.pop(num)
                t_tmp = target_4()
                targets_4 += [t_tmp]
    '''
    if time % 60 == 0:
        t_tmp = target_4()
        targets_4 += [t_tmp]
    '''

    for num_g, j in enumerate(guns):
        g11.move_gun()    
        g11.update()   
        g22.move_gun()    
        g22.update()
        for num, i in enumerate(balls):
            if num_g == 0:
                i.move()
                i.update()
            if i.hittest_gun(j):
                guns.pop(num_g)
                balls.pop(num)     
    
                       
    for num_t, j in enumerate(targets):
        j.move()
        j.update()
        for num, i in enumerate(balls):
            if num_t == 0:
                i.move()
                i.update()
            if i.hittest(j):
            
                print('Good', num)
                balls.pop(num)
                targets.pop(num_t)
                #t_tmp = target_1()
                t_tmp = random.choice([target_1(),target_2(),target_3(),
                                       target_4()])
                targets += [t_tmp]
            
        
    pygame.display.update()
    sc.fill(WHITE)

pygame.quit()
        






       

'''        
    z = 0.03
    t1.live = 1
    while t1.live or balls:
        for b in balls:
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                if mousebutton[0]:
                    g1.fire2_start
                else:
                    g1.fire2_end
                    
                f1 = pg.font.Font(None, 30)    
                text = f1.render('Вы уничтожили цель за ' + str(bullet) + ' выстрелов', 1, (0, 0, 0))
                sc.blit(text, (100, 50))
                
        #sc.update()
        #time.sleep(0.03)
        
        
    #sc.itemconfig(screen1, text='')
    
    #sc.delete(gun)
    #root.after(750, new_game)
'''

