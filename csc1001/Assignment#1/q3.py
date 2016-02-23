# coding=utf-8
# ********************************************************
#   > OS     : Ubuntu 14.04
# 	> Author : JasonGUTU
# 	> Mail   : intergujinjin@foxmail.com
# 	> Time   : 2016/2/5
# ********************************************************
# The Question Three
from AssTools.getInput import get_number


if __name__ == '__main__':
    m = get_number('Enter an integer:', sign=1)
    n = 1
    while n ** 2 < m:
        n += 1
    print(n)
