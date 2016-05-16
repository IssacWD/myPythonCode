# CSC 1001 Assignment #4
####1. Question 1

First of all, I generate a link list with

```py
#!q1.py
link_list = SLList()
    for i in range(10):
        link_list.insert_head(i)
    head_node = link_list.insert_head('head')
```

And traversal it with

```py
#!q1.py
def recursion_count_link_list(head_node, link_list):
    """ recursion to count items in list """
    if head_node.pointer is None:
        return 1
    else:
        return 1 + recursion_count_link_list(head_node.pointer, link_list)
```

### 2. Question 2

The parse function is:

```py
#!q2.py
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
            

def check_if_sub_parent(node):
    """ Check if its sub-node has sub-node """
    if node.left.left is not None and node.left.right is not None:
        return True
    if node.right.left is not None and node.right.right is not None:
        return True
    return False
```

### 3. Question 3

First of all, I set a link list with random integers. And make it into list, sort it with quick sort:

```py
#!q3.py
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
```

And make the sorted list back to link list...



