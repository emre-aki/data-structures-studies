import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Queue.queue import Queue

q = Queue()
q.push(1)
q.push(2)
q.push(0)
q.push(7)
print('q.is_empty(): %r'%(q.is_empty()))
print(str(q))
print('len(q): %d'%(len(q)))
print('\nq.pop(): %s'%(str(q.pop())))
print(str(q))
print('len(q): %d'%(len(q)))
print('\nq.pop(): %s'%(str(q.pop())))
print(str(q))
print('len(q): %d'%(len(q)))
print('\nq.pop(): %s'%(str(q.pop())))
print(str(q))
print('len(q): %d'%(len(q)))
print('\nq.pop(): %s'%(str(q.pop())))
print(str(q))
print('len(q): %d'%(len(q)))
print('q.is_empty(): %r'%(q.is_empty()))