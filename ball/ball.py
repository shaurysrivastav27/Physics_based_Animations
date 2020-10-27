import pygame
import random
import math

SQUARE=600
RADIUS = 50
ball_posx = 1000
ball_posy = 1000
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
        pygame.draw.rect(self.canvas, (0, 128, 128), (30,0, self.width - 60, self.height))     
        

class Ball:
    def __init__(self, posx, posy, rad, table):
        self.posx = ball_posx
        self.posy = ball_posy
        self.rad = RADIUS
        self.table = table
        self.vely = 0
        self.velx = 8
    def draw(self):
        pygame.draw.circle(self.table.canvas, (255,255,0), (self.posx//10, self.posy//10), self.rad)    
    def move(self):
        global point1, point2,GRAVITY



        self.posx += self.velx                                                  ###
        self.posy += self.vely                                                  ###       
        self.vely -= GRAVITY                                                    ###  The mathematical part lies here
        if self.posy >= (self.table.height*10 ):                                ###      
            self.vely = -int(math.floor((self.vely)*0.9))                       ###      



        self.draw() 


table1 = Table(SQUARE,SQUARE)
ball1 = Ball(100,5,RADIUS,table1)
Table_name="Bouncing ball"
run = True
valmove = 0
print("Click to start the animation")
while run:
    table1.draw(Table_name)
    pygame.time.delay(10)
    ball1.draw()
    if(valmove == 1):
        ball1.move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =False   
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos() 
            valmove = 1
            ball1.draw()     
    pygame.draw.rect(table1.canvas, (160,82,45), (100,0, 1,100))  
    pygame.draw.circle(table1.canvas, (160,82,45), (100,100), 15)           
    pygame.draw.rect(table1.canvas, (210,105,30), (570,400, 50, 200))          
    pygame.display.update()
pygame.quit()            

