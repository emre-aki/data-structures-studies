from Queue.node import Node

class Queue:

    def __init__(self):
        self.__top = None    # to remember which node to pop
        self.__bottom = None # to remember after which node to append

    def peek(self):
        return self.__top.data

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.__top = new_node
            self.__bottom = new_node
        else:
            self.__bottom.next = new_node
            self.__bottom = new_node

    def pop(self):
        if not self.is_empty():
            return_this = self.__top.data
            if self.__top == self.__bottom: # if last element present in the queue
                self.__top = None
                self.__bottom = None
            else:
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
        while not (iterator == self.__bottom):
            returnstr += ('%s, '%(str(iterator)))
            iterator = iterator.next
        returnstr += ('%s]'%(str(self.__bottom)))
        return returnstr