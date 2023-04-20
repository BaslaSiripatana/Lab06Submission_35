class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0,color=(0,0,0)):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.color = color
    def draw(self,screen):
        pg.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0, color=(0,0,0)):
        Rectangle.__init__(self, x, y, w, h, color)
    
    def isMouseOn(self):
        #Implement your code here
        px, py = pg.mouse.get_pos()
        if self.x <= px <= self.x+self.w and self.y <= py <= self.y+self.h :
            return True
        else:
            return False
    
    def isMousePress(self):
        mouse_presses = pg.mouse.get_pressed()
        if mouse_presses[0] == 1:
            return True
        else:
            return False

import sys 
import pygame as pg

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100,(220,20,20)) # สร้าง Object จากคลาส Button ขึ้นมา

while(run):
    screen.fill((255, 255, 255))
    if btn.isMousePress():
        btn.color = (120,20,220)
    elif btn.isMouseOn():
        btn.color = (150,150,150)
    else:
        btn.color = (220,20,20)
   
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False

        if event.type == pg.KEYDOWN and event.key == pg.K_d: #ปุ่มถูกกดลงและเป็นปุ่ม D
            print("Key D down")
            btn.x += 20
        if event.type == pg.KEYDOWN and event.key == pg.K_a: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            print("Key A down")
            btn.x -= 20
        if event.type == pg.KEYDOWN and event.key == pg.K_w: #ปุ่มถูกกดลงและเป็นปุ่ม D
            print("Key W down")
            btn.y -= 20
        if event.type == pg.KEYDOWN and event.key == pg.K_s: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            print("Key S down")
            btn.y += 20
        

    btn.draw(screen)
    pg.display.update()