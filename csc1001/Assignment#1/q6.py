# coding=utf-8
#********************************************************
#   > OS     : Ubuntu 14.04
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/2/15
#********************************************************
# The Question Six
from AssTools.getInput import get_number
from math import *


def get_func():
    func = input("Input the function:")
    if func == 'sin':
        return sin
    elif func == 'cos':
        return cos
    elif func == 'tan':
        return tan
    else:
        print("Does not support this function!\nPlease input one of 'sin' 'cos' 'tan'")
        return get_func()


def get_a_b_n():
    a = get_number('Input a:', int_type=False)
    b = get_number('Input b:', int_type=False)
    while b <= a:
        a = get_number('a should be smaller than b\nPlease input a again:', int_type=False)
    n = get_number('Input the number of sub-intervals:', sign=1)
    middleware = (b - a) / n
    return middleware, n, a


def calculate(func, tuple):
    midware = tuple[0]
    n = tuple[1]
    a = tuple[2]
    _sum = 0
    for i in range(1, n + 1):
        _sum += func(a + midware * (i - 0.5))
    return midware * _sum


if __name__ == '__main__':
    print("The result is %s" % calculate(get_func(), get_a_b_n()))
