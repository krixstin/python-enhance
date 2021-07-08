from collections import deque

deque_list = deque()
for i in range(5):
    deque_list.append(i)
deque_list.appendleft(10)
deque_list.appendleft([11,22,33])

#shift to right
deque_list.rotate(3) 

print(deque_list)