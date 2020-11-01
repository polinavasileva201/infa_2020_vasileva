from random import randrange as rnd, choice
import pygame
from pygame.draw import *
from random import randint
import math
import time
pygame.init()

# print (dir(math))
FPS = 50
sc = pygame.display.set_mode((800, 600))
#sc = pygame.display.set_mode((1000, 600))
 
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (255,53,0)

BLACK = (0, 0, 0)
WHITE = (255,255,255)
ORANGE = (254,106,0)
COLORS = [BLUE, GREEN, RED, BROWN]

sc.fill(WHITE)

time = 0


class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
    
        
        color = COLORS[randint(0, 3)]
        self.id = ellipse( sc, color, (self.x - self.r, self.y - self.r,
                                        self.x + self.r, self.y + self.r))
        
        self.live = 30
        
    
    def set_coords(self):
        sc.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        
      
    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        self.x += self.vx
        self.y -= self.vy
        self.vx +=0
        self.vy -= 10

        if self.x < self.r: 
            self.vx *= -1
            self.x = self.r
        if self.x > 800 - self.r:
            self.vx *= -1
            self.x = 800 - self.r
        
        if self.y < self.r: 
            self.vy *= -1
            self.y = self.r
        if self.y > 600 - self.r:
            self.vy *= -1
            self.y = 600 - self.r

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (obj.x - self.x)**2 + (obj.y - self.y)**2 <= obj.r + self.r:
            return True
        # FIXME
        else:
            return False


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = line(sc, BLACK,(20,450),(50,420),7) # FIXME: don't know how to set it...
        #self.id = rect(sc, WHITE,(20,450,30,30))
        
    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.pos[1]-new_ball.y) / (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10


            
    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.id = line(sc, ORANGE,(20,450),(50,420),7)
            #self.id = rect(sc, ORANGE,(20,450,30,30))
            
        else:
            self.id = line(sc, BLACK,(20,450),(int(20 + max(self.f2_power, 20) * math.cos(self.an)),
                    int(450 + max(self.f2_power, 20) * math.sin(self.an))),7)
            #self.id = rect(sc, BLACK,(20,450,30,30))
            
        ###sc.coords(self.id, 20, 450, 20 + max(self.f2_power, 20) * math.cos(self.an), 450 + max(self.f2_power, 20) * math.sin(self.an) )
     
     
    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.id = line(sc, ORANGE,(20,450),(50,420),7)
            #self.id = rect(sc, ORANGE,(20,450,(30),30))
        else:
            self.id = line(sc, BLACK,(20,450),(50,420),7)
            #self.id = rect(sc, BLACK,(20,450,(30),30))


class target():
    def __init__(self):
        self.points = 0
        self.live = 1
        # FIXME: don't work!!! How to call this functions when object is created?
        '''
        color = COLORS[randint(0, 3)]
        self.id = ellipse( sc, color, (0,0,0,0))
        '''
        #self.id_points = sc.create_text(30,30,text = self.points,font = '28')
        
        '''
        myfont = pygame.font.SysFont('Comic Sans MS', 28)
        self.id_points = myfont.render(self.points, False, (0, 0, 0)) 
        sc.blit(self.id_points,(30,30)) 
        '''  

        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 750)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        #color = self.color = 'RED'
        #self.id = ellipse( sc, RED, (x-r, y-r, x+r, y+r))
        self.id = circle( sc, RED, (x, y), r)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.id = ellipse( sc, color, ( -10, -10, -10, -10))
        self.points += points
        #sc.itemconfig(self.id_points, text=self.points)
        myfont = pygame.font.SysFont('Comic Sans MS', 28)
        self.id_points = myfont.render(self.points, False, (0, 0, 0)) 
        sc.blit(self.id_points,(30,30)) 


t1 = target()
#screen1 = sc.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []


pygame.display.update()
clock = pygame.time.Clock()
finished = False

gun, t1, balls, bullet
#gun, t1, screen1, balls, bullet

bullet = 0
balls = []
    
while not finished:
    clock.tick(FPS)
    time += 1
    
    t1.new_target()

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            #exit()
            finished = True
            
        if ev.type == pygame.MOUSEMOTION:
            g1.targetting(ev)
            
        if ev.type == pygame.MOUSEBUTTONDOWN:
            g1.fire2_start(ev)
        if ev.type == pygame.MOUSEBUTTONUP:
            g1.fire2_end(ev)

           

    ''' 
    if pygame.mouse.get_focused():
        pos = pygame.mouse.get_pos()
        g1.targetting(self, pos[0],pos[1])
    
    mousebutton = pygame.mouse.get_pressed()
    if mousebutton[0]:
        pos1 = pygame.mouse.get_pos()
        g1.fire2_start(self,pos1[0],pos1[1])
    else:
        pos2 = pygame.mouse.get_pos()
        g1.fire2_end(self,pos2[0],pos2[1])
    '''
    '''
    if pygame.mouse.get_focused():
        g1.targetting()
    
    mousebutton = pygame.mouse.get_pressed()
    if mousebutton[0]:
        g1.fire2_start()
    else:
        g1.fire2_end()
  
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
        g1.targetting()
        g1.power_up()
        
    #sc.itemconfig(screen1, text='')
    
    #sc.delete(gun)
    #root.after(750, new_game)


    
    pygame.display.update()
    sc.fill(WHITE)

pygame.quit()




'''
def new_game(event=''):
    global gun, t1, screen1, balls, bullet
    t1.new_target()
    bullet = 0
    balls = []
    
    mousebutton = pygame.mouse.get_pressed()
    if mousebutton[0]:
        g1.fire2_start
    else:
        g1.fire2_end

    if pygame.mouse.get_focused():
        g1.targetting

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
        g1.targetting()
        g1.power_up()
        
    sc.itemconfig(screen1, text='')
    
    sc.delete(gun)
    root.after(750, new_game)


new_game()

#mainloop()



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    time += 1

    pygame.display.update()
    sc.fill(WHITE)


pygame.quit()

'''
