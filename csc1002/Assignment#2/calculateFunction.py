# coding=utf-8
# ********************************************************
#   > OS     : Ubuntu 14.04
# 	> Author : JasonGUTU
# 	> Mail   : intergujinjin@foxmail.com
# 	> Time   : 2016/2/26
# ********************************************************
import os, sys, re

VARIABLE = ['x', 'X', 'y', 'Y']

class InputError(BaseException):
    def __init__(self, value):
        print('==================================\nWrong Input! %s\n   AND THE PROGRAM WILL RESTART' % value)
        if input('==================================\nIf you want to exit, input \'terminate\':') != 'terminate':
            pythonInterpreter = sys.executable
            os.execl(pythonInterpreter, pythonInterpreter, * sys.argv)


class Equation():
    def __init__(self, string):
        str_list = list(string)
        for i in range(len(str_list)):
            if str_list[i] in VARIABLE and i != 0:
                if str_list[i - 1].isdigit() or str_list[i - 1] == '(' or str_list[i - 1] == ')':
                    str_list[i] = '*' + str_list[i]
        func_list_with = ''.join(str_list).split('=')
        if func_list_with[1].startswith('-'):
            func_list_with[1] = '+' + func_list_with[1][1:]
        else:
            func_list_with[1] = '-' + func_list_with[1]
        self.string =  ''.join(func_list_with)

    def get_arguments(self):
        try:
            constant = eval(self.string.replace('x', '0').replace('y', '0').replace('X', '0').replace('Y', '0'))
            coefficient_x = eval(self.string.replace('x', '1').replace('X', '1').replace('y', '0').replace('Y', '0')) - constant
            coefficient_y = eval(self.string.replace('y', '1').replace('Y', '1').replace('x', '0').replace('X', '0')) - constant
        except NameError:
            raise InputError('The variable must be \'x\' or \'y\'')
        return [coefficient_x, coefficient_y, (-1) * constant]


def calculate_mat(list_mat):
    return list_mat[0][0] * list_mat[1][1] - list_mat[0][1] * list_mat[1][0]


def calculate_point(list_argument_1, list_argument_2):  # [a, b, c] for 'ax + by = c'
    D_mat = calculate_mat([list_argument_1[:2], list_argument_2[:2]])
    X_mat = calculate_mat([[list_argument_1[2], list_argument_1[1]], [list_argument_2[2], list_argument_2[1]]])
    Y_mat = calculate_mat([[list_argument_1[0], list_argument_1[2]], [list_argument_2[0], list_argument_2[2]]])
    if D_mat == 0: raise InputError('Parallel lines exist!')
    x = X_mat / D_mat ; y = Y_mat / D_mat
    return (x, y)


def calculate_line_point(point_A, point_B):
    return ((point_A[0] - point_B[0]) ** 2 + (point_A[1] - point_B[1]) ** 2) ** 0.5


def calculate_area(func_str1, func_str2, func_str3):
    E_1 = Equation(func_str1).get_arguments() ; E_2 = Equation(func_str2).get_arguments() ; E_3 = Equation(func_str3).get_arguments()
    point1, point2, point3 = calculate_point(E_1, E_2), calculate_point(E_2, E_3), calculate_point(E_3, E_1)
    a, b, c = calculate_line_point(point1, point2), calculate_line_point(point2, point3), calculate_line_point(point3, point1)
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def get_input():
    string = input('Please input function: ')
    if len(re.compile(r'=').findall(string)) != 1:
        raise InputError('Please input an equation!')
    return string


if __name__ == '__main__':
    while True:
        print('==================================')
        area = calculate_area(get_input(), get_input(), get_input())
        print('The area of the triangle is %.4f' % area)
        if input('If you want to exit, input \'terminate\':') == 'terminate':
            break
    print('===DONE===')