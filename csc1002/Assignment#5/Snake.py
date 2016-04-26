# coding=utf-8
# ********************************************************
#   > OS     : OS X 10.11.3
#   > Author : JasonGUTU
#   > Mail   : intergujinjin@foxmail.com
#   > Time   : 2016/4/22
# ********************************************************
# Extend from 'snakeTemplateTpStudent.py'
from tkinter import *
from random import randint


# global variable for size of this game
WIDTH = 15
HEIGHT = 10
CELL_WIDTH = 40
CELL_HEIGHT = 40
# The approximate center point as the snake initial position
SNAKE_INIT_BODY_SEGMENT = [[HEIGHT//2, WIDTH//2]]
DIRECTION_ARRAY = [[-1, 0], [0, 1], [1, 0], [0, -1]]


class Snake:
    """ base class for snake """
    def __init__(self, init_length_of_snake=1, init_segment=SNAKE_INIT_BODY_SEGMENT, direction='E'):
        self.__length = init_length_of_snake
        self.__body_segment = init_segment
        self.__direction = direction
        self.__about_to_eat = False

    def get_length(self):
        return self.__length

    def get_body_segment(self):
        return self.__body_segment

    def get_direction(self):
        return self.__direction

    def set_direction(self, direction):
        self.__direction = direction

    def add_body_segment(self, additional_segment):
        self.__body_segment.insert(0, additional_segment)
        self.__length += 1

    def about_to_eat_apple(self):
        self.__about_to_eat = True
        self.__length += 1

    def if_game_over(self):
        buffer_list = list()
        for segment in self.__body_segment:
            if segment in buffer_list:
                return True
            else:
                for segment in self.__body_segment:
                    if not 0 < segment[0] < HEIGHT:
                        return True
                    elif not 0 < segment[1] < WIDTH:
                        return True
                buffer_list.append(segment)
        return False

    def move(self):
        direction_index = int()
        if self.__direction == 'N':
            direction_index = 0
        elif self.__direction == 'E':
            direction_index = 1
        elif self.__direction == 'S':
            direction_index = 2
        elif self.__direction == 'W':
            direction_index = 3
        additional_segment = [self.__body_segment[0][0] + DIRECTION_ARRAY[direction_index][0],
                             self.__body_segment[0][1] + DIRECTION_ARRAY[direction_index][1]]
        self.__body_segment.insert(0, additional_segment)
        if self.__about_to_eat:
            self.__about_to_eat = False
        else:
            self.__body_segment.pop()
            self.__about_to_eat = False


def DrawBackground():
    'Refresh the background to all yellow.'
    for i in range(HEIGHT):
        for j in range(WIDTH):
            labelArray[i][j].configure(bg='yellow')


def DrawSnake():
    'Draw the snake in the background.'
    for segment in snake.get_body_segment():
        labelArray[segment[0]][segment[1]].configure(bg='brown')


def DrawFood():
    'Draw the food'
    foodImage = PhotoImage(file='apple.gif')
    labelArray[food[0]][food[1]].configure(image=foodImage)
    labelArray[food[0]][food[1]].photo = foodImage


def IsFoodInWay():
    'If food is in the next position ahead, return True. Otherwise, return False.'
    direction_index = int()
    if snake.get_direction() == 'N':
        direction_index = 0
    elif snake.get_direction() == 'E':
        direction_index = 1
    elif snake.get_direction() == 'S':
        direction_index = 2
    elif snake.get_direction() == 'W':
        direction_index = 3
    body_segment = snake.get_body_segment()
    head = body_segment[0]
    next_head = [head[0]+DIRECTION_ARRAY[direction_index][0],
                head[1]+DIRECTION_ARRAY[direction_index][1]]
    if food == next_head:
        return True
    else:
        return False


def GoGoGo():
    """ continously movement of the snake"""
    global food  # global var in function, you niubi!
    keep_on_moving = True
    # while not snake.if_game_over():
    if IsFoodInWay():
        # snake.add_body_segment(food)
        snake.about_to_eat_apple()
        labelText.configure(text='Snake Length: %s' % snake.get_length())
        labelArray[food[0]][food[1]].configure(image='')
        food = [randint(1, HEIGHT-2), randint(1, WIDTH-2)]
    snake.move()
    DrawBackground()
    DrawSnake()
    DrawFood()
    if keep_on_moving:  # Hint: this is related to question (2) and (3)
        root.after(500, GoGoGo)
    # labelText.configure(text='Game Over! Your score is: %s' % snake.get_length())



def SetDirectionN(event):
    snake.set_direction('N')


def SetDirectionS(event):
    snake.set_direction('S')


def SetDirectionW(event):
    snake.set_direction('W')


def SetDirectionE(event):
    snake.set_direction('E')


if __name__ == '__main__':
    snake = Snake()  # init Sanke
    food = [5, 10]  # Initial position of food
    root = Tk()
    root.title('Snake')
    root.geometry('%sx%s+50+50' % (WIDTH * CELL_WIDTH, HEIGHT * CELL_HEIGHT + 40))
    labelText = Label(root, text='Snake Length: %s' %
                                 snake.get_length(), font=('Times New Roman', 16))
    labelText.place(x=0, y=0, width=CELL_WIDTH * WIDTH, height=CELL_HEIGHT)
    labelArray = []
    for i in range(HEIGHT):
        labelRow = []
        for j in range(WIDTH):
            labelRow.append(Label(root, text='%s,%s' % (i, j), bg='yellow'))
            labelRow[j].place(
                x=j * CELL_WIDTH, y=(i + 1) * CELL_HEIGHT, width=CELL_WIDTH, height=CELL_HEIGHT)
        labelArray.append(labelRow[:])
    DrawBackground()
    DrawSnake()
    GoGoGo()

    root.bind("<KeyRelease-Up>", SetDirectionN)
    root.bind("<KeyRelease-Down>", SetDirectionS)
    root.bind("<KeyRelease-Left>", SetDirectionW)
    root.bind("<KeyRelease-Right>", SetDirectionE)

    root.mainloop()



