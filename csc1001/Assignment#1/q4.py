# coding=utf-8
#********************************************************
#   > OS     : Ubuntu 14.04
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/2/5
#********************************************************
# The Question Four

from AssTools.getInput import get_number

def display(number):
    print("m      m+1    m**(m+1)")
    for i in range(number):
        print(format(i + 1, '<6d'), format(i + 2, '<6d'), (i + 1) ** (i + 2))

if __name__ == '__main__':
    display(get_number('Please input a integer:', sign=1))

