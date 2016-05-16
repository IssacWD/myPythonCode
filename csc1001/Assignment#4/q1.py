#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Author : JasonGUTU
Email  : hellojasongt@gmail.com

Qeustion One"""
from SLList import SLList, Node


def recursion_count_link_list(head_node, link_list):
    """ recursion to count items in list """
    if head_node.pointer is None:
        return 1
    else:
        return 1 + recursion_count_link_list(head_node.pointer, link_list)


if __name__ == '__main__':  # for testing
    link_list = SLList()
    for i in range(10):
        link_list.insert_head(i)
    head_node = link_list.insert_head('head')
    print(recursion_count_link_list(head_node, link_list))
    # The return is 11, which is 10 + 1
