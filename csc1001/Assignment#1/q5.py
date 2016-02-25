# coding=utf-8
#********************************************************
#   > OS     : Ubuntu 14.04
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/2/5
#********************************************************
# The Question Five
from AssTools.getInput import get_number
import time


def algorithm_Eratosthenes(max_number):
    import math
    list_of_bool = [True] * (max_number + 1)
    list_of_bool[0] = list_of_bool[1] = False
    for i in range(2, math.ceil(math.sqrt(max_number))):
        if not list_of_bool[i]:
            continue
        for j in range(i * i, max_number + 1, i):
            list_of_bool[j] = False
    return list_of_bool


def display(list_of_bool):
    prime_number_list = list()
    for i in range(len(list_of_bool)):
        if list_of_bool[i]:
            prime_number_list.append(i)
    for i in range(len(prime_number_list)):
        if (i + 1) % 8 == 0:
            print(format(prime_number_list[i], '<9d'), end='\n')
        else:
            print(format(prime_number_list[i], '<9d'), end='')


if __name__ == '__main__':
    number = get_number('Enter an integer:', sign=1)
    if number <= 2:
        print('Do not have any number that meet the requirements!')
    else:
        print('The prime numbers smaller than %s include:' % number)
        a = time.clock()
        _list = algorithm_Eratosthenes(number)
        b = time.clock()
        display(_list)
        c = time.clock()
        print('\n %s \n %s \n %s' % (b - a, c - b, c - a))



