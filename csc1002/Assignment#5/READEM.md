#CSC1002 Assignment #5

###1. `Snake` class
Class Snake is the base class to presentate snake in the map.
Structure:
```
class Snake
    |- __init__(self, init_length_of_snake=1, init_segment=SNAKE_INIT_BODY_SEGMENT, direction='E'))
    |- get_length(self)
    |- get_body_segment(self)
    |- get_direction(self)
    |- set_direction(self, direction)
    |- add_body_segment(self, additional_segment)
    |- about_to_eat_apple(self)
    |- if_game_over(self)
    |_ move(self)
```
Method move make the snake move.
Method if_game_over() return wheter the game is over.

In Function GoGoGo():
```python
#!Snake.py
def GoGoGo():
    """ Continously movement of the snake"""
    global food  # global var in function, you niubi!
    if snake.if_game_over():
        keep_on_moving = False
        labelText.configure(text='Game Over! Your score is: %s' % snake.get_length())
        return
    else:
        keep_on_moving = True
    if IsFoodInWay():
        # snake.add_body_segment(food)
        snake.about_to_eat_apple()
        labelText.configure(text='Snake Length: %s' % snake.get_length())
        labelArray[food[0]][food[1]].configure(image='')
        food = FoodGenerator()
    snake.move()
    DrawBackground()
    DrawSnake()
    DrawFood()
    if keep_on_moving:  # Hint: this is related to question (2) and (3)
        root.after(500, GoGoGo)
```
This is the core function in the game program.
###2. How to run
In your terminal, run`python Snake.py`
when you eat your self, or touch the wall, game over.