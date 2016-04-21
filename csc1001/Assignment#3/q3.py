# coding=utf-8
# ********************************************************
#   > OS     : OS X 10.11.3
#   > Author : JasonGUTU
#   > Mail   : intergujinjin@foxmail.com
#   > Time   : 2016/4/20
# ********************************************************
# The Question Three
from random import shuffle
from random import randint


class River:

    """ A base class for this strange ecosystem """

    def __init__(self, length_of_river, bears_number, fishes_number):
        river_list = list()
        for i in range(bears_number):
            river_list.append('B')
        for i in range(fishes_number):
            river_list.append('F')
        for i in range(length_of_river - bears_number - fishes_number):
            river_list.append('N')
        shuffle(river_list)
        self.river = river_list

    def _generate_baby(self, parents_type):
        number_of_empty = self.river.count('N')
        if number_of_empty == 0:
            return
        baby_position_of_empty = randint(1, number_of_empty)
        this_empty = 0
        for position, item in enumerate(self.river):
            if item == 'N':
                this_empty += 1
            if this_empty == baby_position_of_empty:
                self.river[position] = parents_type
                break

    def _iter(self):
        last_action = int()
        last_type = str()
        for position, item in enumerate(self.river):
            if item == 'N':
                continue
            else:
                action = randint(-1, 1)
                next_position = position + action
                if next_position >= len(self.river) or next_position < 0:
                    continue
                if action == 0:
                    continue
                else:
                    if last_action == 1 and last_type == item:
                        continue
                    if self.river[next_position] == item:
                        self._generate_baby(item)
                    elif self.river[next_position] == 'N':
                        self.river[next_position] = item
                        self.river[position] = 'N'
                    else:
                        if item == 'B':
                            self.river[next_position] = 'B'
                            self.river[position] = 'N'
                        else:
                            self.river[position] = 'N'
                last_type = item
                last_action = action

    def move(self, steps=1):
        for time in range(steps):
            self._iter()

    def show(self):
        show_repr = str()
        for item in self.river:
            if item == 'N':
                show_repr += '  '
            elif item == 'F':
                show_repr += 'F '
            else:
                show_repr += 'B '
        return show_repr

    def print_lines(self, times):
        for i in range(times):
            self.move()
            print('|' + self.show() + '|')


def main():
    print('''========================================================================
This is a strange river, two kinds of creatures live in here, bears and fishes.
You can tell me the length of river, number of bears and fishes.
And you can tell me how many steps you want to see. So let's start.
========================================================================
''')
    length_of_river = int(
        input('1. Please tell me the length of this river(integer only):'))
    number_of_bear = int(
        input('2. How many bears do we initially have(integer only):'))
    number_of_fishes = int(
        input('3. How many fish do we initially have(integer only):'))
    times_you_want_see = int(
        input('4. How many times do you want to see(integer only):'))
    river = River(length_of_river, number_of_bear, number_of_fishes)
    river.print_lines(times_you_want_see)


if __name__ == '__main__':
    main()
