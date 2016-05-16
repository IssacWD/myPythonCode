#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Author : JasonGUTU
Email  : hellojasongt@gmail.com

quit sort for link list """
from SLList import SLList, Node

def generate_link_list():
    print('Generating link list...')
    link_list = SLList()
    list_number = [200, 135, 20, 122, 97, 200, 116, 199, 34, 30, 140, 184, 173, 113, 48, 83, 119, 23, 7, 144]
    print('The list is :')
    for number in list_number:
        print(number, end=', ')
    print()
    for number in list_number:
        link_list.insert_head(number)
    return link_list


def partition(number_list, start_index, end_index):
    standard_number = number_list[start_index]
    standard_index = start_index
    for i in range(start_index + 1, end_index + 1):
        if number_list[i] < standard_number:
            number_list.insert(standard_index, number_list.pop(i))
            standard_index += 1
    return standard_index


def quit_sort(number_list, start_index, end_index):
    if start_index <= end_index:
        mid_index = partition(number_list, start_index, end_index)
        quit_sort(number_list, start_index, mid_index - 1)
        quit_sort(number_list, mid_index + 1, end_index)


def sort_SLList(SLList_):
    number_list = list()
    for number in SLList_.iterate():
        number_list.append(number)
    print('Sorting...')
    quit_sort(number_list, 0, len(number_list) - 1)
    result_SLList = SLList()
    print('The sort result is:')
    for number in number_list:
        print(number, end=', ')
        result_SLList.insert_tail(number)
    return result_SLList


if __name__ == '__main__':
    sort_SLList(generate_link_list())



