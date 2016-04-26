# coding=utf-8
# ********************************************************
#	> OS     : Ubuntu 14.04
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/1/22
# ********************************************************
# For Testing performance of list, set and tuple

def deco_time(func):
    def in_deco_time(n):
        import time
        start = time.clock()
        func(n)
        end = time.clock()
        cost_time = (end - start) * 1000
        return cost_time
    return in_deco_time


@deco_time
def list_create(n):
    __list = list(i for i in range(n))


@deco_time
def set_create(n):
    __set = set(i for i in range(n))


@deco_time
def tuple_create(n):
    __tuple = tuple(i for i in range(n))


def main():
    tmp = [100, 500, 1000, 2000, 4000, 8000, 20000, 100000, 500000, 1000000, 5000000, 10000000, 50000000]
    data_list = {tmp[i]: 0 for i in range(len(tmp))}
    data_set = data_list.copy()
    data_tuple = data_list.copy()
    for i in range(len(tmp)):
        data_list[tmp[i]] = list_create(tmp[i])
        data_set[tmp[i]] = set_create(tmp[i])
        data_tuple[tmp[i]] = tuple_create(tmp[i])
    print('        '+'|'+'    list'+'|'+'     set'+'|'+'   tuple')
    for i in range(len(tmp)):
        print(format(tmp[i],"8d")+format(data_list[tmp[i]], "9.2f")+format(data_set[tmp[i]], "9.2f")+format(data_tuple[tmp[i]], "9.2f"))

main()
