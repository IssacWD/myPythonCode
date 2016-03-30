# coding=utf-8
#********************************************************
#   > OS     : Ubuntu 15.10
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/3/30
#********************************************************
# The Question One

def get_next_guess(num, last_guess):
    next_guess = (last_guess + (num / last_guess)) / 2
    if abs(next_guess - last_guess) > accuracy_parameter:
        return get_next_guess(num, next_guess)
    else: return next_guess


def sqrt(num):
    init_guess = 1
    return get_next_guess(num, init_guess)


if __name__ == '__main__':
    accuracy_parameter = 0.00001
    number = eval(input('Please input a number:'))
    print('The sqrt of this number is %.6f' % sqrt(number))