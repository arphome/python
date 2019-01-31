from tkinter import *

#def SnakeDraw(canvas):



def growSnake(snakeFollow,number):
    placement = length - 1
    while number > 0:
        c = canvas.coords(snakeFollow[placement])
        s = canvas.create_rectangle(c, fill="red", tags = "snake")
        canvas.move(s,-50, 0)
        number = number - 1
        placement = placement + 1
        snakeFollow.append(s)
        
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

canvas.pack()



canvas.bind_all('<KeyPress-Right>', MoveRectangle)
canvas.bind_all('<KeyPress-Left>', MoveRectangle)
canvas.bind_all('<KeyPress-Up>', MoveRectangle)
canvas.bind_all('<KeyPress-Down>', MoveRectangle)
                
#Draws the head


s = canvas.create_rectangle(160,10,210,60, fill="blue",tags="snake")


snakeFollow.append(s)

length = len(snakeFollow)



growSnake(snakeFollow,number)

    
#SnakeDraw(canvas)

root.mainloop()


