# coding=utf-8
#********************************************************
#   > OS     : Ubuntu 14.04
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/2/15
#********************************************************
# The Question Six


import math


def get_func():
    func = input("Input the function:")
    if func == 'sin':
        return math.sin
    elif func == 'cos':
        return math.cos
    elif func == 'tan':
        return math.tan
    else:
        print("Does not support this function!\nPlease input one of 'sin' 'cos' 'tan'")
        return get_func()


def get_a_b_n():
    a = eval(input("Input a:"))
    b = eval(input("Input b:"))
    while b <= a:
        a = eval(input("a should be smaller than b\nPlease input a again:"))
    n = int(input("Input the number of sub-intervals:"))
    middleware = (b - a) / n
    return middleware, n, a


def calculate(func, tuple):
    midware = tuple[0]
    n = tuple[1]
    a = tuple[2]
    _sum = 0
    for i in range(n):
        _sum += func(a + midware * (i - 0.5))
    return midware * _sum


if __name__ == '__main__':
    print("The result is %s" % calculate(get_func(), get_a_b_n()))
