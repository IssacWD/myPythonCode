#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Author : JasonGUTU
Email  : hellojasongt@gmail.com

Question number four. """


def print_step(start_stack, end_stack):
    name_list = ['A', 'B', 'C']
    print('  %s --> %s' % (name_list[start_stack], name_list[end_stack]))


def get_minimum():
    top_plate_list = list()
    for index, stack in enumerate(stack_pool):
        if len(stack) == 0:
            top_plate_list.append((n + 1, index))
        else:
            top_plate_list.append((stack[-1], index))
    top_plate_list.sort()
    if top_plate_list[0][0] != last_move[0]:
        return top_plate_list[0][1], top_plate_list[0][0]
    else:
        return top_plate_list[1][1], top_plate_list[1][0]


def move():
    min_stack, min_plate = get_minimum()
    next_1 = (min_stack + 1) % 3
    next_2 = (min_stack + 2) % 3
    last_move[0] = min_plate
    if len(stack_pool[next_1]) == 0 or stack_pool[next_1][-1] > min_plate:
        stack_pool[next_1].append(stack_pool[min_stack].pop())
        print_step(min_stack, next_1)
    else:
        stack_pool[next_2].append(stack_pool[min_stack].pop())
        print_step(min_stack, next_2)


if __name__ == '__main__':
    n = int(input('Hoe many plates in this tower(integer only): '))
    stack_pool = [[], [], []]
    for i in range(n, 0, -1):
        stack_pool[0].append(i)
    last_move = [0]
    while True:
        if len(stack_pool[1]) == n or len(stack_pool[2]) == n:
            break
        move()
    print(' Finished. ')
