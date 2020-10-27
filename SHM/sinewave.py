import pygame
import random
import math

SQUARE=600
RADIUS = 50
ball_posx = 2800
ball_posy = 3000
AMPLITUDE = 1500
freq = 0.08
GRAVITY = -10
class Table:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.canvas = canvas = pygame.display.set_mode((self.width,self.height))
    def draw(self, st):
        self.canvas = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption(st)
        self.canvas.fill((0,0,0))
        pygame.draw.rect(self.canvas, (225,225,225), (30,0, self.width - 60, self.height),2)     
        

class Ball:
    def __init__(self, posx, posy, rad, table):
        self.posx = ball_posx
        self.posy = ball_posy
        self.rad = RADIUS
        self.table = table
        self.vely = 0
        self.velx = 0
    def draw(self):
        pygame.draw.circle(self.table.canvas, (255,255,0), (self.posx//10, self.posy//10), self.rad)    
    def move(self,t):
        global point1, point2,GRAVITY


        self.posy = int(ball_posy + AMPLITUDE * math.sin(freq*t))               ### The mathematical part lies here


        self.draw() 


table1 = Table(SQUARE,SQUARE)
ball1 = Ball(100,5,RADIUS,table1)
Table_name="Sinewave"
run = True
valmove = 0
print("Click to start the animation")
time = 0
while run:
    time += 1
    table1.draw(Table_name)
    pygame.time.delay(10)
    pygame.draw.rect(table1.canvas, (160,82,45), (ball_posx//10-2,0, 4,ball1.posy//10))
    pygame.draw.rect(table1.canvas, (0, 128, 128), (0,150, 600,1))            
    pygame.draw.rect(table1.canvas, (0, 128, 128), (0,450, 600,1))            
    ball1.draw()
    if(valmove == 1):
        ball1.move(time)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =False   
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos() 
            valmove = 1
            ball1.draw()    
    pygame.display.update()
pygame.quit()            

