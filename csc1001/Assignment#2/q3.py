# coding=uft-8
#********************************************************
#   > OS     : Ubuntu 15.10
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/3/30
#********************************************************
# The Question Three

def sum_of_double_even_place(list_even_place_number):
    sum = 0
    for number in list_even_place_number:
        sum += get_digit(number * 2)
    return sum


def get_digit(double_number):
    if double_number < 10: return double_number
    splited = list(str(double_number))
    return int(splited[0]) + int(splited[1])


def sum_of_odd_place(list_odd_place_number):
    return sum(list_odd_place_number)


def is_valid(number_str):
    odd_number_list = list()
    even_number_list = list()
    for index, value in enumerate(list(number_str[::-1])):
        if index % 2 == 0:
            odd_number_list.append(int(value))
        else:
            even_number_list.append(int(value))
    if (sum_of_double_even_place(even_number_list) + sum_of_odd_place(odd_number_list)) % 10 == 0:
        return True
    else:
        return False


def get_input_number():
    input_str = input('Please input the number of card:')
    if not input_str.isdigit():
        print('Please input a number:')
        return get_input_number()
    return input_str


if __name__ == '__main__':
    if is_valid(get_input_number()):
        print('This card number is valid!')
    else:
        print('This card number is invalid!')