class Node:

    def __init__(self, data):
        self.__data = data
        self.__left = None
        self.__right = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @data.deleter
    def data(self):
        del self.__data

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        self.__left = value

    @left.deleter
    def left(self):
        del self.__left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value):
        self.__right = value

    @right.deleter
    def right(self):
        del self.__right

    def __str__(self):
        return '%s' % (self.__data)

    def __repr__(self):
        return '%r' % (self.__data)