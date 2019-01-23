from tkinter import *

#def SnakeDraw(canvas):



def growSnake(snakeFollow,number):
    placement = length - 1
    while number > 0:
        c = snakeFollow[placement]
        s = canvas.create_rectangle(c, fill="red", tags = "snake")
        canvas.move(s,-50, 0)
        snake.append(s)
        number = number - 1
        placement = placement + 1
        snakeFollow.append(canvas.coords(s))
        new.append(canvas.coords(s))
    print (snake)

def MoveRectangle(event):
    moved = False
    SnakeLength = length - 1
    moveSnake = SnakeLength - 1
    if SnakeLength >= 0:
        canvas.coords(snake[SnakeLength], snake[moveSnake])
        SnakeLength - 1
        moveSnake - 1
    if event.keysym == 'Up':
        canvas.move(snake[0], 0, -50)
        moved = True
    elif event.keysym == 'Down':
        canvas.move(snake[0], 0, 50)
        moved = True
    elif event.keysym == 'Right':
        canvas.move(snake[0], 50, 0)
        moved = True
    elif event.keysym == 'Left':
        canvas.move(snake[0],-50, 0)
        moved = True
            


root=Tk()

canvas = Canvas(width=1000, height=1000)
snake0 = ''
snake1 = ''
snake2 = ''
snake3 = ''
snakeFollow = [] #snakeFollow is a list that contains coords of snake parts
number = 2
new = []

canvas.pack()



canvas.bind_all('<KeyPress-Right>', MoveRectangle)
canvas.bind_all('<KeyPress-Left>', MoveRectangle)
canvas.bind_all('<KeyPress-Up>', MoveRectangle)
canvas.bind_all('<KeyPress-Down>', MoveRectangle)
                
#Draws the head
snake = []

s = canvas.create_rectangle(160,10,210,60, fill="blue",tags="snake")
snake.append(s)

snakeFollow.append(canvas.coords("snake"))

length = len(snakeFollow)

growSnake(snakeFollow,number)

#SnakeDraw(canvas)

root.mainloop()


