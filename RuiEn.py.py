from tkinter import *

def SnakeDraw(canvas):
    moved = True
    global where_am_i1
    global snake0
    global snake1
    global snake2
    global snake3
    if moved == True:
        snake3 = canvas.create_rectangle(10,10,60,60, fill="blue",tags="snake")
        snake2 = canvas.create_rectangle(where_am_i2, fill="blue",tags="snake")
        snake1 = canvas.create_rectangle(where_am_i1, fill="blue",tags="snake")
        moved = False

def growSnake(snakeFollow,number):
    while number > 0:
        placement = length - 1
        c = snakeFollow[placement]
        s = canvas.create_rectangle(c, fill="blue", tags="snake")
        snakeFollow.append(c)
        canvas.move(snakeFollow[placement], -50, 0)
        print(snakeFollow)
        number = number - 1

def MoveRectangle(event):
    moved = False
    if event.keysym == 'Up':
        canvas.move("snake", 0, -50)
        moved = True
    elif event.keysym == 'Down':
        canvas.move("snake", 0, 50)
        moved = True
    elif event.keysym == 'Right':
        canvas.move("snake", 50, 0)
        moved = True
    elif event.keysym == 'Left':
        canvas.move("snake",-50, 0)
        moved = True
    where_am_i1 = canvas.coords(snake0)
    print(where_am_i1)
    where_am_i2 = canvas.coords(snake1)
    print(where_am_i2)
    where_am_i3 = canvas.coords(snake2)
    print(where_am_i3)
    where_am_i4 = canvas.coords(snake3)
    print(where_am_i4)

root=Tk()

canvas = Canvas(width=500, height=500)
snake0 = ''
snake1 = ''
snake2 = ''
snake3 = ''
snakeFollow = [] #snakeFollow is a list that contains coords of snake parts
number = 2
canvas.pack()

canvas.bind_all('<KeyPress-Right>', MoveRectangle)
canvas.bind_all('<KeyPress-Left>', MoveRectangle)
canvas.bind_all('<KeyPress-Up>', MoveRectangle)
canvas.bind_all('<KeyPress-Down>', MoveRectangle)
                
#Draws the head
snake = canvas.create_rectangle(160,10,210,60, fill="blue",tags="snake")

snakeFollow.append(canvas.coords(snake))

print(snakeFollow)

length = len(snakeFollow)
                
growSnake(snakeFollow,number)

SnakeDraw(canvas)

root.mainloop()





