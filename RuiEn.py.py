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
    y = x + 35
    xx = random.randint(25,750)
    yy = xx + 35
    circle = canvas.create_oval(x, xx,y, yy, outline='black', fill='red')
    apple = apple - 1
    print (apple)
    shapes.append(circle)
    while moved == True:
        
def snakeTouchApple(x, y, x1, y1):
    if (abs(x - x1) <= 50) and (abs(y - y1) <= 50):
        canvas.delete(apple)
     
def MoveRectangle(event):
    moved = False
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
number = 5
c = ""
event = ""
apple = 1
shapes = []
canvas.pack()



canvas.bind_all('<KeyPress-Right>', MoveRectangle)
canvas.bind_all('<KeyPress-Left>', MoveRectangle)
canvas.bind_all('<KeyPress-Up>', MoveRectangle)
canvas.bind_all('<KeyPress-Down>', MoveRectangle)
                
#Draws the head
y1 = 250
x1 = 300
xx1 = x1 + 50
yy1 = y1 + 50

s = canvas.create_rectangle(x1,xx1,y1,yy1, fill="blue",tags="snake")


snakeFollow.append(s)

length = len(snakeFollow)


growSnake(snakeFollow,number)

appleMaker(apple)

    
#SnakeDraw(canvas)

root.mainloop()


