# coding=utf-8
#********************************************************
#   > OS     : Ubuntu 14.04
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/2/20
#********************************************************
import re

def get_number(num_str, int_type=True, sign=0, length=0):
    number = input(num_str)
    if int_type:
        if sign == 0:
            if not re.compile(r'-?[1-9]\d*').match(number):
                print('Unvalidated Input! Please input again!')
                return get_number(num_str, int_type=True, sign=sign, length=length)
        elif sign == 1:
            if not re.compile(r'[1-9]\d*').match(number):
                print('Unvalidated Input! Please input again!')
                return get_number(num_str, int_type=True, sign=sign, length=length)
        elif sign == -1:
            if not re.compile(r'-[1-9]\d*').match(number):
                print('Unvalidated Input! Please input again!')
                return get_number(num_str, int_type=True, sign=sign, length=length)
        else:
            print('Unvalidated Input! Wrong argument in the method!')
            return get_number(num_str, int_type=True, sign=sign, length=length)
    else:
        if sign == 0:
            if not re.compile(r'-?([1-9]\d*\.\d*|0\.\d*[1-9]\d*|0?\.0+|0)').match(number):
                if not re.compile(r'-?[1-9]\d*').match(number):
                    print('Unvalidated Input! Please input again!')
                    return get_number(num_str, int_type=False, sign=sign, length=length)
        elif sign == 1:
            if not re.compile(r'[1-9]\d*\.\d*|0\.\d*[1-9]\d*|0?\.0+|0').match(number):
                if not re.compile(r'[1-9]\d*').match(number):
                    print('Unvalidated Input! Please input again!')
                    return get_number(num_str, int_type=False, sign=sign, length=length)
        elif sign == -1:
            if not re.compile(r'-([1-9]\d*\.\d*|0\.\d*[1-9]\d*)').match(number):
                if not re.compile(r'-[1-9]\d*').match(number):
                    print('Unvalidated Input! Please input again!')
                    return get_number(num_str, int_type=False, sign=sign, length=length)
        else:
            print('Unvalidated Input! Wrong argument in the method!')
            return get_number(num_str, int_type=False, sign=sign, length=length)
    if length != 0:
        if len(number) > length:
            print('Unvalidated Input! Please check the length of your input!')
            return get_number(num_str, int_type=int_type, sign=sign, length=length)
    return eval(number)


def get_money(money_str):
    pass

def get_char(char_str, length=0):
    pass