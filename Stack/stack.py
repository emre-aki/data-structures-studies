from Stack.node import Node

class Stack:

    def __init__(self):
        self.__top = None

    def peek(self):
        return self.__top.data

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.__top = new_node
        else:
            new_node.next = self.__top
            self.__top = new_node

    def pop(self):
        if not self.is_empty():
            return_this = self.__top.data
            self.__top = self.__top.next
            return return_this
        return None

    def is_empty(self):
        return self.__top is None

    def __len__(self):
        count_nodes = 0
        iterator = self.__top
        while iterator is not None:
            count_nodes += 1
            iterator = iterator.next
        return count_nodes

    def __str__(self):
        if self.is_empty():
            return '[]'
        returnstr = '['
        iterator = self.__top
        while iterator.next is not None:
            returnstr += ('%s, '%(str(iterator)))
            iterator = iterator.next
        returnstr += ('%s]'%(str(iterator)))
        return returnstr