from tkinter import *
import random
import time
#def SnakeDraw(canvas):



def growSnake(snakeFollow,number):
    placement = length - 1
    while number > 0:
        c = canvas.coords(snakeFollow[placement])
        s = canvas.create_rectangle(c, outline = 'cyan', fill="sky blue", tags = "snake")
        canvas.move(s,-50, 0)
        number = number - 1
        placement = placement + 1
        print (placement)
        snakeFollow.append(s)
        
def appleMaker(apple):
  while apple >= 0:
    x = random.randint(25,600)
    xx = x + 50
    y = random.randint(25,600)
    yy = y + 50
    circle = canvas.create_oval(x, y,xx, yy, outline='white', fill='red')
    apple = apple - 1
    appleC.append(circle)
        
def snakeTouchApple():

    Coords = canvas.coords(appleC[0])
    ax = Coords[0]
    axx = Coords[1]
    ay = Coords[2]
    ayy = Coords[3]
    coords = canvas.coords(snakeFollow[0])
    x1 = coords[0]
    xx1 = coords[1]
    y1 = coords[2]                                                               
    yy1 = coords[3]
    if ((abs(x1 - ax) <= 50) and (abs(y1 - ay) <= 50) and (abs(xx1 - axx) <= 50) and (abs(yy1 - ayy) <= 50)):
        print ("YUMM!")
        apple = appleC[0]
        appleC.remove(appleC[0])
        canvas.delete(apple)
        appleMaker(0)
        growSnake(snakeFollow,number)
        ScoreCounter(text)

def ScoreCounter(text):
    global score
    score = score + 1
    canvas.delete("scoretag")
    canvas.create_text(75, 25, text= 'score =', font = ('Robot', 30))
    text = canvas.create_text(175, 28, text= score, font = ('Robot', 30), tag = "scoretag")
    
def MoveRectangle(event):
    moved = True
    if moved == True:
        snakeTouchApple()
        CheckBox()
        TouchTail()
    SnakeLength = len(snakeFollow) - 1
    moveSnake = SnakeLength - 1
    while moveSnake >= 0:
        if SnakeLength >= 1:
            canvas.coords(snakeFollow[SnakeLength], canvas.coords(snakeFollow[moveSnake]))
            SnakeLength = SnakeLength - 1             
            moveSnake = moveSnake - 1
        elif moveSnake == 0:
            SnakeLength = len(snakeFollow) - 1
            moveSnake = SnakeLength - 1
    if event.keysym == 'Up':
        canvas.move(snakeFollow[0], 0, -50)
        moved = True
    if event.keysym == 'Down':
        canvas.move(snakeFollow[0], 0, 50)
        moved = True
    if event.keysym == 'Right':
        canvas.move(snakeFollow[0], 50, 0)
        moved = True
    if event.keysym == 'Left':
        canvas.move(snakeFollow[0],-50, 0)
        moved = True

def TouchTail():
    coords = canvas.coords(snakeFollow[0])
    x1 = coords[0]
    y1= coords[1]
    x2 = coords[2]                                                               
    y2 = coords[3]
    lengthtails= len(snakeFollow) - 1
    coordstails = canvas.coords(snakeFollow[lengthtails])
    tailx1 = coordstails[0]
    taily1 = coordstails[1]
    tailx2 = coordstails[2]
    taily2 = coordstails[3]
    while lengthtails > 0:
        if (abs(x1 - tailx1) <= 50) and (abs(y1 - taily1) <= 50) and (abs(x2 - tailx2) <= 50) and (abs(y2 - taily2) <= 50):
            print ("Game Over")
            lengthtails = 0
        else:
            lengthtails = lengthtails - 1
    
def CheckBox():
    coords = canvas.coords(snakeFollow[0])
    x1 = coords[0]
    y1= coords[1]
    x2 = coords[2]                                                               
    y2 = coords[3]
    if (abs(x1 < 50)) or (abs(y1 < 50)) or (abs(x2 > 950)) or (abs(y2 > 950)):
        print ("Game OVER")
        
root=Tk()

canvas = Canvas(width=1000, height=1000)
snakeFollow = [] #snakeFollow is a list that contains coords snake canvas parts
number = 1
circle = ""
appleC = []
c = ""
event = ""
apple = 0 #number of apples
canvas.pack()
textlist = []


canvas.bind_all('<KeyPress-Right>', MoveRectangle)
canvas.bind_all('<KeyPress-Left>', MoveRectangle)
canvas.bind_all('<KeyPress-Up>', MoveRectangle)
canvas.bind_all('<KeyPress-Down>', MoveRectangle)
                
#Draws the head
y1 = 150
x1 = 200
xx1 = x1 + 50
yy1 = y1 + 50
score = 0
lengthtails = 0

#Test Coords to hold the coords for the apple
ax = 0
axx = 0
ay = 0
ayy = 0
Coords = []
coords = []
text = ""

canvas.create_rectangle(50,50,950,950, outline='red', fill="black")

s = canvas.create_rectangle(x1,xx1,y1,yy1, outline='sky blue', fill="cyan",tags="snake")

snakeFollow.append(s)

length = len(snakeFollow)

growSnake(snakeFollow,number)

appleMaker(apple)

ScoreCounter(text)

#SnakeDraw(canvas)

root.mainloop()




