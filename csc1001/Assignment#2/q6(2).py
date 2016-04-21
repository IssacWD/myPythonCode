# coding=utf-8
#********************************************************
#   > OS     : Ubuntu 15.10
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/3/30
#********************************************************
# The Question Six

def is_conflict(status_tuple, next_row_place):
    this_row_number = len(status_tuple)
    if next_row_place in status_tuple: return True
    for row_number, place in enumerate(status_tuple):
        left_right = place - row_number ; right_left = place + row_number
        if (next_row_place - this_row_number == left_right) or (next_row_place + this_row_number == right_left):
            return True
    return False


def generater(queen_number, status_tuple=()):
    for position in range(queen_number):
        if not is_conflict(status_tuple, position):
            if len(status_tuple) == queen_number - 1:
                yield (position,)
            else:
                for next_result in generater(queen_number, status_tuple + (position,)):
                    yield (position,) + next_result


def find_all_queens(queen_number):
    queens_list = list(generater(queen_number))
    return queens_list


def find_a_queens(all_list):
    from random import choice
    return choice(all_list)


def print_queens(status_tuple):
    for place in status_tuple:
        print('| ' * place + '|Q' + '| ' * (8 - place))


if __name__ == '__main__':
    print_queens(find_a_queens(find_all_queens(8)))


