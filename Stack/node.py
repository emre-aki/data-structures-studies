class Node:

    def __init__(self, data):
        self.__data = data
        self.__next = None

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
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

    @next.deleter
    def next(self):
        del self.__next

    def __str__(self):
        return '%s' % (self.__data)

    def __repr__(self):
        return '%r' % (self.__data)