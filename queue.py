# your code goes here
#queue using list
#the enque and deque operation takes o(n) time
list1=[]
list1.append(1)
list1.append(2)
list1.append(3)
print(list1)
print(list1.pop(0))
print(list1.pop(0))
print(list1.pop(0))
print(list1)

#queue using deque from collections
#the enque and deque operation takes o(1) time
from collections import deque
q=deque()
print(q)
q.append(1)
q.append(2)
q.append(3)
print(q)
print(q.popleft())

from collections import deque

# Initializing a queue
q = deque()

# Adding elements to a queue
q.append('a')
q.append('b')
q.append('c')

print("Initial queue")
print(q)

# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)
