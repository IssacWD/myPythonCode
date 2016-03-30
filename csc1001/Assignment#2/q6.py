# coding=utf-8
#********************************************************
#   > OS     : Ubuntu 15.10
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/3/30
#********************************************************
# The Question Six

import itertools
import random

def get_valid_solution():
    valid_solutions_list = list()
    queens_status_list = list(range(8))
    for vec in itertools.permutations(queens_status_list):
        if (len(set(vec[i] - i for i in range(8))) == 8) and (len(set(vec[i] + i for i in range(8))) == 8):
            valid_solutions_list.append(vec)
    return random.choice(valid_solutions_list)


def print_eight_queens(status_list):
    for i in range(8):
        print('| ' * status_list[i] + '|Q' + '| ' * (8 - status_list[i]))


if __name__ == '__main__':
    print_eight_queens(get_valid_solution())
