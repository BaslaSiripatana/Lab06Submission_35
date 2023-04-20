class InputBox:

    def __init__(self, x, y, w, h, text='', digitonly = False):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.digitonly = digitonly
    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if (self.digitonly and event.unicode.isdigit()) or not(self.digitonly):
                        self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)

class Text:

    def __init__(self, x, y, text=''):
        self.color = COLOR_TEXT
        self.x = x
        self.y = y
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.x, self.y))

class Rectangle():
    def __init__(self,x=0,y=0,w=0,h=0,color=(0,0,0), text = ''):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.color = color
        self.colortext = COLOR_TEXT
        self.text = text
        self.txt_surface = FONT.render(text, True, self.colortext)
    def draw(self,screen):
        pg.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h))
        screen.blit(self.txt_surface, (self.x+5, self.y+5))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0, color=(0,0,0), text = ''):
        Rectangle.__init__(self, x, y, w, h, color, text)
    
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
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
COLOR_TEXT = (0,0,0)
FONT = pg.font.Font(None, 32)

input_box1 = InputBox(180, 100, 140, 32) # สร้าง InputBox1
input_box2 = InputBox(180, 150, 140, 32) # สร้าง InputBox2
input_box3 = InputBox(180, 200, 140, 32, '', True)
input_boxes = [input_box1, input_box2, input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย

input_text1 = Text(30, 105, "Firstname: ")
input_text2 = Text(30, 155, "Lastname: ")
input_text3 = Text(30, 205, "Age: ")
input_texts = [input_text1, input_text2, input_text3]

btn = Button(30,300,100,32,(204,114,245), "SUBMIT")

output_state = False

run = True

while run:
    screen.fill((255, 255, 255))
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
    
    for text in input_texts:
        text.draw(screen)

    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    if btn.isMouseOn():
        btn.color = (7, 185, 252)
    else:
        btn.color = (204,114,245)
    if btn.isMousePress() and btn.isMouseOn():
        out_text = "Hello " + input_boxes[0].text + " " + input_boxes[1].text + " ! You are " + input_boxes[2].text + " years old."
        output_text = Text(30, 370, out_text)
        output_state = True

    if output_state:
        output_text.draw(screen)    

    btn.draw(screen)
    pg.time.delay(1)
    pg.display.update()