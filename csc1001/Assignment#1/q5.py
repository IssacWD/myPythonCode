# coding=utf-8
#********************************************************
#   > OS     : Ubuntu 14.04
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/2/5
#********************************************************
# The Question Five


def get_number_and_judge():
    number = input("Enter an integer:")
    if not number.isdigit():
        print("Wrong input")
        number = get_number_and_judge()
    if eval(number) <= 2:
        print("Don't have any number.")
        number = get_number_and_judge()
    return int(number)


def Judge(number):
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


def prime_list(Number):
    prime_list_ = [2]
    for i in range(3, Number, 2):
        if Judge(i):
            prime_list_.append(i)
    return prime_list_


def display(list):
    print(len(list))
    for i in range(len(list)):
        if i % 7 == 0:
            print(format(list[i], '<8d'), end='\n')
        else:
            print(format(list[i], '<8d'), end='')



N = get_number_and_judge()
print('The prime numbers smaller than %s include:' % N)
display(prime_list(N))