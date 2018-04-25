import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Queue.queue_with_stacks import QueueWithStacks

qws = QueueWithStacks()
qws.push(1)
qws.push(2)
qws.push(3)
qws.push(4)
qws.push(5)
print(str(qws))
qws.pop()
print(str(qws))
qws.push(1)
print(str(qws))
qws.pop()
print(str(qws))