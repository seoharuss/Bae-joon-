import sys
from collections import deque

def bfs(variable):
  queue = deque([variable])
  while queue:
    variable = queue.popleft()
    if variable == k:
      return array[variable]
    for i in (variable-1, variable+1, 2*variable):
      if 0 <= i < MAX and not array[i]:
        array[i] = array[variable] + 1
        queue.append(i)

MAX = 100001
n, k = map(int, sys.stdin.readline().split())
array = [0] * MAX
print(bfs(n))
