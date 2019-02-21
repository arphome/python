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
        
def appleMaker(apple, x, xx, y, yy):
  print(x,y,xx,yy)
  while apple >= 0:
    x = random.randint(25,750)
    xx = x + 50
    y = random.randint(25,750)
    yy = y + 50
    circle = canvas.create_oval(x, y,xx, yy, outline='black', fill='red')
    apple = apple - 1
    shapes.append(circle)
    print(x,y,xx,yy)
        
def snakeTouchApple():
    print(x,y,xx,yy)
    coords = canvas.coords(snakeFollow[0])
    x1 = coords[0]
    y1 = coords[1]
    xx1 = coords[2]
    yy1 = coords[3]
    print (x1 - x)
    print (y1 - y)
    print (xx1 - x)
    print (yy1 - yy)
    print ((abs(x1 - x) <= 50) and (abs(y1 - y) <= 50) and (abs(xx1 - xx) <= 50) and (abs(yy1 - yy) <= 50))
    if ((abs(x1 - x) <= 50) and (abs(y1 - y) <= 50) and (abs(xx1 - xx) <= 50) and (abs(yy1 - yy) <= 50)):
        print ("apple")
        canvas.delete(shapes[0])

     
def MoveRectangle(event):
    print(x,y,xx,yy)
    moved = True
    if moved == True:
        snakeTouchApple()
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
apple = 0
shapes = []
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
x = 0
xx = 0
y = 0
yy = 0

s = canvas.create_rectangle(x1,xx1,y1,yy1, fill="blue",tags="snake")


snakeFollow.append(s)

length = len(snakeFollow)

growSnake(snakeFollow,number)

appleMaker(apple, x, xx, y, yy)

    
#SnakeDraw(canvas)

root.mainloop()




