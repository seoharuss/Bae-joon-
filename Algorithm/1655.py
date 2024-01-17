import heapq
import sys

n = int(sys.stdin.readline())

leftHeap = []
rightHeap = []
for i in range(n):
  num = int(sys.stdin.readline())

  if len(leftHeap) == len(rightHeap):
    heapq.heappush(leftHeap, -num)
  else:
    heapq.heappush(rightHeap, num)

  if rightHeap and rightHeap[0] < -leftHeap[0]:
    leftValue = heapq.heappop(leftHeap)
    rightValue = heapq.heappop(rightHeap)

    heapq.heappush(leftHeap, -rightValue)
    heapq.heappush(rightHeap, -leftValue)

  print(-leftHeap[0])
  
#######################################
# 1. 링크드리스트 만들기 
# 링크드리스트로 값을 하나하나 집어넣고 출력한다.

# 2. 힙을 2개를 사용하여 구현하기