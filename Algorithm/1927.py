from heapq import heappush, heappop
import sys

heap = []
N = int(sys.stdin.readline())
for _ in range(N):
  push = int(sys.stdin.readline())
  if push == 0:
    if len(heap) == 0:
      print(0)
    else:
      print(heappop(heap))
  elif push != 0:
    heappush(heap, push)
