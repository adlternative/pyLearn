import collections

cq = collections.deque([1, 1, 3, 4])
print(cq)
cq.append(2)
print(cq)
cq.popleft()

# cq.append(1)
# cq.append(2)
print(cq)

