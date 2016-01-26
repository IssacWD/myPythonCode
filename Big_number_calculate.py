# coding=utf-8
# ********************************************************
#	> OS     : Ubuntu 14.04
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/1/22
# ********************************************************

# This class for calculate the number bigger than 2^32 even more

class BigNumber:
    def __init__(self, string_of_number):
        string_without_space = string_of_number.strip()
        list_two_part = string_without_space.split('.')
        self.__list_each_int = list(list_two_part[0])
        self.__list_each_float = list(list_two_part[1])

    def __add__(self, another_BigNumber):
        pass

    def __sub__(self, another_BigNumber):


    def __mul__(self, another_BigNumber):

    def __truediv__(self, another_BigNumber):

    def __float__(self):

    def __int__(self):

    def __str__(self):

    def __cmp__(self, another_BigNumber):

    def __le__(self, another_BigNumber):

    def __lt__(self, another_BigNumber):

    def __ge__(self, another_BigNumber):

    def __gt__(self, another_BigNumber):

    def __getitem__(self, index):

