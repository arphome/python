from tkinter import *
import random
#def SnakeDraw(canvas):



def growSnake(snakeFollow,number):
    placement = length - 1
    while number > 0:
        c = canvas.coords(snakeFollow[placement])
        s = canvas.create_rectangle(c, fill="green", tags = "snake")
        canvas.move(s,-50, 0)
        number = number - 1
        placement = placement + 1
        snakeFollow.append(s)
        
def appleMaker(apple):
  while apple >= 0:
    x = random.randint(25,750)
    xx = x + 50
    y = random.randint(25,750)
    yy = y + 50
    circle = canvas.create_oval(x, y,xx, yy, outline='black', fill='red')
    apple = apple - 1
    appleC.append(circle)
        
def snakeTouchApple(score):
    print (appleC)
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
        score = score + 1
        print (score)
        
def MoveRectangle(event):
    moved = True
    if moved == True:
        snakeTouchApple(score)
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
    elif event.keysym == 'Down':
        canvas.move(snakeFollow[0], 0, 50)
        moved = True
    elif event.keysym == 'Right':
        canvas.move(snakeFollow[0], 50, 0)
        moved = True
    elif event.keysym == 'Left':
        canvas.move(snakeFollow[0],-50, 0)
        moved = True       


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



canvas.bind_all('<KeyPress-Right>', MoveRectangle)
canvas.bind_all('<KeyPress-Left>', MoveRectangle)
canvas.bind_all('<KeyPress-Up>', MoveRectangle)
canvas.bind_all('<KeyPress-Down>', MoveRectangle)
                
#Draws the head
y1 = 0
x1 = 50
xx1 = x1 + 50
yy1 = y1 + 50

#Test Coords to hold the coords for the apple
score = 0
ax = 0
axx = 0
ay = 0
ayy = 0
Coords = []

s = canvas.create_rectangle(x1,xx1,y1,yy1, fill="blue",tags="snake")

snakeFollow.append(s)

length = len(snakeFollow)

growSnake(snakeFollow,number)

appleMaker(apple)

    
#SnakeDraw(canvas)

root.mainloop()

