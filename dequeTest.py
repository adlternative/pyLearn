from collections import deque
q =deque(range(5))
q.append(5)
q.appendleft(6)
q.pop()
q.popleft()
q.rotate(-4)
print(q)
