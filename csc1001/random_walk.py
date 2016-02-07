# coding=utf-8
#********************************************************
#   > OS     : Ubuntu 14.04
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/2/5
#********************************************************
# Happy new year!
import random

def choose():
    l_or_r = [True, False]
    return random.choice(l_or_r)

def display(location):
    print(' ' * (15 + location), '*', ' ' * (15 - location))

def main():
    location = 0
    print(' ' * 15, '*',' ' * 15)
    steps = 50
    for i in range(steps):
        if choose():
            location += 1
        else:
            location -= 1
        display(location)

main()
