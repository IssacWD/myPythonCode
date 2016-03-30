# coding=utf-8
#********************************************************
#   > OS     : Ubuntu 15.10
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/3/30
#********************************************************
# The Question Two
def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def deco_display(func):
    count = [1]
    def print_number(number):
        if count[0] % 10 == 0:
            count[0] += 1
            print(format(number, '<8d'))
        else:
            count[0] += 1
            print(format(number, '<8d'), end='')
    return print_number


@deco_display
def print_ten_per_line(number):
    pass


def is_emirp(number):
    if is_prime(number):
        reverse_number = int(str(number)[::-1])
        if is_prime(reverse_number):
            return True
    return False


if __name__ == '__main__':
    number_of_emirp = int(input('Please input the number of emirps you want:'))
    index = 0
    number = 10
    while index < number_of_emirp:
        if is_emirp(number):
            print_ten_per_line(number)
            index += 1
        number += 1