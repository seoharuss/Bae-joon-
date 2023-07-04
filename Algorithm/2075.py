import heapq

queue = []
n = int(input())

for _ in range(n):
  arr = list(map(int, input().split()))
  for j in arr:
    if len(queue) < n:
      heapq.heappush(queue, j)
    else:
      if queue[0] < j:
        heapq.heappush(queue, j)
        heapq.heappop(queue)
print(queue[0])
