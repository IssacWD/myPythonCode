class Node:
    def __init__(self, element, pointer=None):
        self.element = element
        self.pointer = pointer


class SLList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_head(self, e):
        newest = Node(e, None)
        newest.pointer = self.head
        self.head = newest
        if self.is_empty():
            self.tail = newest
        self.size += 1
        return newest

    def insert_tail(self, e):
        newest = Node(e, None)
        if self.is_empty():
            self.head = newest
        else:
            self.tail.pointer = newest
        self.tail = newest
        self.size += 1
        return newest

    def delete_head(self):
        if self.head is None:
            print('The list is empty.')
        else:
            element = self.head.element.copy()
            self.head = self.head.pointer
            self.size -= 1
            return element

    def iterate(self):
        pointer = self.head
        # print('The element in the list: ')
        while pointer is not None:
            result = pointer.element
            pointer = pointer.pointer
            yield result
