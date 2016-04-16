# coding=utf-8
# ********************************************************
#   > OS     : OS X 10.11.3
# 	> Author : JasonGUTU
# 	> Mail   : intergujinjin@foxmail.com
# 	> Time   : 2016/4/16
# ********************************************************
# The Question Three
from random import choice, random
from itertools import permutations

class Creatures:
    """ Base class for creatures """
    def action(self):
        return choice([-1, 0, 1])

class Bear(Creatures):
    """ A class for bears. """
    def __init__(self):
        self.bear = True
        self.action = int()

    def set_action(self, ):


    def __repr__(self):
        return '<Bear>'


class Fish(Creatures):
    """ A class for fishes. """
    def __init__(self):
        self.fish = True

    def __repr__(self):
        return '<Fish>'


class Empty:
    """ A class for empty location in the river """
    def __init__(self):
        self.last = None

    def __repr__(self):
        return '<Empty>'


class River:
    """ The ecosystem consists of bears and fishes. """
    def __init__(self, number_of_cell, number_of_fishes, number_of_bears):
        self.__river_list = list()
        for i in range(number_of_bears):
            self.__river_list.append([Bear()])
        for i in range(number_of_fishes):
            self.__river_list.append([Fish()])
        for i in range(number_of_cell - number_of_bears - number_of_fishes):
            self.__river_list.append([Empty()])
        self.__river_list = choice(permutations(self.__river_list))

    def move(self, steps=1, show=True):
        for i in range(steps):
            self._move_by_step()
            if show:
                print(self.show())

    def _move_by_step(self):
        buffer_list = self.__river_list[:]
        for position, item in enumerate(buffer_list):
            if not isinstance(item, Empty):
                action = item.action()
                next_position = position + action
                if action == 0: continue
                if next_position < 0: continue
                buffer_list[position] = Empty()
                buffer_list[next_position].append(item)
        for position, item in enumerate(buffer_list):
            if len(item) != 1:
                if isinstance(item[0], Empty):
                    








    def show(self):
        show_repr = str()
        for item in self.__river_list:
            if isinstance(item, Empty):
                show_repr += 'N '
            elif isinstance(item, Fish):
                show_repr += 'F '
            else:
                show_repr += 'B '
        return show_repr

    def _random_decide(self):
        choice_poor = [True, False]
        return choice(choice_poor)

    def __repr__(self):
        return self.show()

