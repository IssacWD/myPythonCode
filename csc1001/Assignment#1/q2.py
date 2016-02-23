# coding=utf-8
#********************************************************
#   > OS     : Ubuntu 14.04
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/2/5
#********************************************************
# The Question Two
from AssTools.getInput import get_number
from math import ceil, log10

if __name__ == '__main__':
    number = get_number('Enter an integer:', sign=1)
    digits = ceil(log10(number))
    output_list = list()
    rest = number
    for i in range(digits - 1, -1, -1):
        output_list.append(rest // (10 ** i))
        rest = rest % (10 ** i)
    for i in output_list:
        print(i)

