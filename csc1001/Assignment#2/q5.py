# coding=utf-8
#********************************************************
#   > OS     : Ubuntu 15.10
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/3/30
#********************************************************
# The Question Five

def change(n, locker_status):
    for i in range(n - 1, len(locker_status)):
        locker_status[i] = not locker_status[i]


if __name__ == '__main__':
    locker_status = [True] * 100
    for i in range(1, 100):
        change(i, locker_status)
    for index, value in enumerate(locker_status):
        if value:
            print(format(index, '<3d'), end='')