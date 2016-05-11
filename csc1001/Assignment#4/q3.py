#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Author : JasonGUTU
Email  : hellojasongt@gmail.com"""


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

