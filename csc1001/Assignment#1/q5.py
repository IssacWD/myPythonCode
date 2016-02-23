# coding=utf-8
#********************************************************
#   > OS     : Ubuntu 14.04
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/2/5
#********************************************************
# The Question Five
from AssTools.getInput import get_number

def Judge(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def prime_list(number):
    prime_list_ = [2]
    for i in range(3, number):
        if Judge(i):
            prime_list_.append(i)
    return prime_list_


def display(list):
    for i in range(len(list)):
        if (i + 1) % 8 == 0:
            print(format(list[i], '<8d'), end='\n')
        else:
            print(format(list[i], '<8d'), end='')


if __name__ == '__main__':
    number = get_number('Enter an integer:', sign=1)
    if number <= 2:
        print('Do not have any number that meet the requirements!')
    else:
        print('The prime numbers smaller than %s include:' % number)
        display(prime_list(number))