#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Author : JasonGUTU
Email  : hellojasongt@gmail.com"""
from LBTree import LBTree


def generate_equation():
    """ the equation is ((3 + 1) * 3) / ((9 - 5) + 2) - ((3 * (7 - 4)) + 6 )
    the result will be -13.0"""
    equation = LBTree()
    equation.add_root('-')
    equation.add_left(equation.root, '/')
    equation.add_right(equation.root, '+')
    equation.add_left(equation.root.left, '*')
    equation.add_right(equation.root.left, '+')
    equation.add_right(equation.root.left.right, '2')
    equation.add_left(equation.root.left.right, '-')
    equation.add_right(equation.root.left.right.left, '5')
    equation.add_left(equation.root.left.right.left, '9')
    equation.add_left(equation.root.left.left, '+')
    equation.add_right(equation.root.left.left, '3')
    equation.add_left(equation.root.left.left.left, '3')
    equation.add_right(equation.root.left.left.left, '1')
    equation.add_right(equation.root.right, '6')
    equation.add_left(equation.root.right, '*')
    equation.add_left(equation.root.right.left, '3')
    equation.add_right(equation.root.right.left, '-')
    equation.add_right(equation.root.right.left.right, '4')
    equation.add_left(equation.root.right.left.right, '7')
    return equation, equation.find_root()


def check_if_sub_parent(node):
    """ Check if its sub-node has sub-node """
    if node.left.left is not None and node.left.right is not None:
        return True
    if node.right.left is not None and node.right.right is not None:
        return True
    return False


def parse_tree(tree_root):
    """ recursionly to parse this tree """
    if not check_if_sub_parent(tree_root):
        calculate = eval(str(tree_root.left.element) + str(tree_root.element) + str(tree_root.right.element))
        tree_root.left = None ; tree_root.right = None
        tree_root.element = calculate
        if tree_root is not root_reference:
            parse_tree(tree_root.parent)
        else:
            print(' ' + str(calculate))
    else:
        if tree_root.left.left is None and tree_root.left.right is None:
            parse_tree(tree_root.right)
        else:
            parse_tree(tree_root.left)


if __name__ == '__main__':
    equation, root_reference = generate_equation()
    print('The result of "((3 + 1) * 3) / ((9 - 5) + 2) - ((3 * (7 - 4)) + 6 )" is :', end='')
    parse_tree(root_reference)





