# Revise the coding to add:
# (1) Clear the cell index text as they are only for your design stage.
# (2) Check if the snake bites itself. If it does, stop motion. Show 'Snake bites itself!' and the final length in Label.
# (3) Check if the snake gets out of the boundary. If it does, stop motion. Show 'Snake gets out of the window!' and the final length in Label.
# (4) In the current coding, there is posiblity that the food will be generated randomly onto the snake body. Revise the coding to prevent from this.
from tkinter import *
import random


width = 15
height = 10
cellWidth = 40
cellHeight = 40
# The approximate center point as the snake initial position
snakeInitialBodySegment = [[height//2, width//2]]
directionArray = [[-1, 0], [0, 1], [1, 0], [0, -1]]


class Snake():

    def __init__(self, length=1, bodySegment=snakeInitialBodySegment, direction='N'):
        self.__length = length
        self.__bodySegment = snakeInitialBodySegment
        self.__direction = direction

    def getLength(self):
        return self.__length

    def getBodySegment(self):
        return self.__bodySegment

    def getDirection(self):
        return self.__direction

    def setDirection(self, direction):
        self.__direction = direction

    def addBodySegment(self, additionalSegment):
        self.__bodySegment.insert(0, additionalSegment)
        self.__length += 1

    def move(self):
        if self.__direction == 'N':
            directionIndex = 0
        elif self.__direction == 'E':
            directionIndex = 1
        elif self.__direction == 'S':
            directionIndex = 2
        elif self.__direction == 'W':
            directionIndex = 3
        additionalSegment = [self.__bodySegment[0][0]+directionArray[directionIndex][0],
                             self.__bodySegment[0][1]+directionArray[directionIndex][1]]
        self.__bodySegment.insert(0, additionalSegment)
        self.__bodySegment.pop()


def DrawBackground():
    'Refresh the background to all yellow.'
    for i in range(height):
        for j in range(width):
            labelArray[i][j].configure(bg='yellow')


def DrawSnake():
    'Draw the snake in the background.'
    for segment in snake.getBodySegment():
        labelArray[segment[0]][segment[1]].configure(bg='brown')


def DrawFood():
    'Draw the food'
    foodImage = PhotoImage(file='apple.gif')
    labelArray[food[0]][food[1]].configure(image=foodImage)
    labelArray[food[0]][food[1]].photo = foodImage


def GoGoGo():
    'Continously movement of the snake'
    global food
    keepOnMoving = True
    if IsFoodInWay():
        snake.addBodySegment(food)
        labelText.configure(text='Snake Length: %s' % snake.getLength())
        labelArray[food[0]][food[1]].configure(image='')
        food = [random.randint(1, height-2), random.randint(1, width-2)]
    snake.move()
    DrawBackground()
    DrawSnake()
    DrawFood()
    if keepOnMoving:  # Hint: this is related to question (2) and (3)
        root.after(500, GoGoGo)


def IsFoodInWay():
    'If food is in the next position ahead, return True. Otherwise, return False.'
    if snake.getDirection() == 'N':
        directionIndex = 0
    elif snake.getDirection() == 'E':
        directionIndex = 1
    elif snake.getDirection() == 'S':
        directionIndex = 2
    elif snake.getDirection() == 'W':
        directionIndex = 3
    bodySegment = snake.getBodySegment()
    head = bodySegment[0]
    nextHead = [head[0]+directionArray[directionIndex][0],
                head[1]+directionArray[directionIndex][1]]
    if food == nextHead:
        return True
    else:
        return False


def SetDirectionN(event):
    snake.setDirection('N')


def SetDirectionS(event):
    snake.setDirection('S')


def SetDirectionW(event):
    snake.setDirection('W')


def SetDirectionE(event):
    snake.setDirection('E')


snake = Snake()
food = [5, 10]  # Initial position of food
root = Tk()
root.title('Snake')
root.geometry('%sx%s+50+50' % (width*cellWidth, height*cellHeight+40))
labelText = Label(root, text='Snake Length: %s' %
                  snake.getLength(), font=('Times New Roman', 16))
labelText.place(x=0, y=0, width=cellWidth*width, height=cellHeight)
labelArray = []
for i in range(height):
    labelRow = []
    for j in range(width):
        labelRow.append(Label(root, text='%s,%s' % (i, j), bg='yellow'))
        labelRow[j].place(
            x=j*cellWidth, y=i*cellHeight+cellHeight, width=cellWidth, height=cellHeight)
    labelArray.append(labelRow[:])
DrawBackground()
DrawSnake()
GoGoGo()


root.bind("<KeyRelease-Up>", SetDirectionN)
root.bind("<KeyRelease-Down>", SetDirectionS)
root.bind("<KeyRelease-Left>", SetDirectionW)
root.bind("<KeyRelease-Right>", SetDirectionE)

root.mainloop()
