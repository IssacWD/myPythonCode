# coding=utf-8
#********************************************************
#   > OS     : Ubuntu 14.04
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/2/5
#********************************************************

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
def algorithm_Eratosthenes(number):


@deco_time
def algorithm_Judge(number):


@deco_time
def algorithm_fusion_judge_erato(number):
