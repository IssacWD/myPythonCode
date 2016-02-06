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
        number_of_prime = func(n)
        end = time.clock()
        cost_time = (end - start) * 1000
        return cost_time, number_of_prime
    return in_deco_time


def algorithm_Eratosthenes(max_number):
    if max_number < 2:
        return [], 0
    list_of_number = [i for i in range(3, max_number, 2)]
    for number in list_of_number:
        for i in range(2, max_number // number):
            try:
                list_of_number.remove(number * i)
            except ValueError:
                continue
    return list_of_number, len(list_of_number)



def Judge(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    for i in range(3, int(number ** 0.5) + 1, 1):
        if number % i == 0:
            return False
    return True


# def algorithm_fusion_judge_erato(number):


# @deco_time
def algorithm_Judge(max_number):
    if max_number < 2:
        return [], 0
    if max_number == 2:
        return [2], 1
    list_of_prime = [2]
    for i in range(3, max_number, 2):
        if Judge(i):
            list_of_prime.append(i)
    return list_of_prime, len(list_of_prime)

# def main():
for i in algorithm_Eratosthenes(10000)[0]:
    if i not in algorithm_Judge(10000)[0]:
        print(i)