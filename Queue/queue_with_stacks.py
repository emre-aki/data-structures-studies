import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Stack.stack import Stack

class QueueWithStacks:

	def __init__(self):
		self.__s1 = Stack()
		self.__s2 = Stack()

	def push(self, data):
		self.__s1.push(data)

	def pop(self):
		while not self.__s1.is_empty():
			self.__s2.push(self.__s1.pop())
		ret = self.__s2.pop()
		while not self.__s2.is_empty():
			self.__s1.push(self.__s2.pop())
		return ret

	def __str__(self):
		if self.__s1.is_empty():
			return '[]'
		while not self.__s1.is_empty():
			self.__s2.push(self.__s1.pop())
		returnstr = '['
		while len(self.__s2) > 1:
			iterator = self.__s2.pop()
			returnstr += ('%s, '%(str(iterator)))
			self.__s1.push(iterator)
		iterator = self.__s2.pop()
		returnstr += ('%s]'%(str(iterator)))
		self.__s1.push(iterator)
		return returnstr