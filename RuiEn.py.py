from tkinter import *

#def SnakeDraw(canvas):


def growSnake(snakeFollow,number):
    while number > 0:
        placement = length - 1
        c = snakeFollow[placement]
        snakeFollow.append(c)
        s = canvas.create_rectangle(c, fill="red")
        S.move(snakeFollow[placement], -50, 0)
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
    
root=Tk()

canvas = Canvas(width=500, height=500)
snake0 = ''
snake1 = ''
snake2 = ''
snake3 = ''
snakeFollow = [] #snakeFollow is a list that contains coords of snake parts
number = 1
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

#SnakeDraw(canvas)

root.mainloop()


