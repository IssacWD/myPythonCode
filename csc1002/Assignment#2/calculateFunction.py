# coding=utf-8
# ********************************************************
#   > OS     : Ubuntu 14.04
# 	> Author : JasonGUTU
# 	> Mail   : intergujinjin@foxmail.com
# 	> Time   : 2016/2/26
# ********************************************************
EQUAL_SIGN = '='
OPERATOR = ['+', '-', '*', '/']
BLANK = ''

def get_function_string():
    function_string = input('Please input function string:')
    return function_string


def sort_function(function_string):
    mid_list = function_string.replace('-', '+-').split('=')
    list_for_element = mid_list[0].split('+')
    for item in mid_list[1].split('+'):
        if item.startswith('-'):
            list_for_element.append(item[1:])
        else:
            list_for_element.append('-' + item)
    dict_variable = {'x':0, 'y':0, 'const':0}
    for item in list_for_element:
        if item == '':
            continue
        elif item[-1] == 'x':
            dict_variable['x'] += eval(item[:-1])
        elif item[-1] == 'y':
            dict_variable['y'] += eval(item[:-1])
        else:
            dict_variable['const'] += eval(item)
    return [dict_variable['x'], dict_variable['y'], dict_variable['const']]


def calculate_area(list_of_argument):  # [a, b, c] for 'ax + by + c = 0'
    pass