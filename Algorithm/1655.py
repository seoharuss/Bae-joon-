import sys
import heapq
N = int(sys.stdin.readline())

minHeap = []
maxHeap = []
answer = []

for i in range(N):
  temp = int(sys.stdin.readline())
  if len(minHeap) == len(maxHeap):
    heapq.heappush(minHeap, (-temp, temp))
  else:
    heapq.heappush(maxHeap, (temp, temp))
  
  if maxHeap and minHeap[0][1] > maxHeap[0][0]:
    temp1 = heapq.heappop(maxHeap[0])
    temp2 = heapq.heappop(minHeap[1])
    heapq.heappush(minHeap, (-temp1, temp1))
    heapq.heappush(maxHeap, (temp2, temp2))
  answer.append(minHeap[0][1])

for j in answer:
  print(j)
  
#######################################
# 1. 링크드리스트 만들기 
# 링크드리스트로 값을 하나하나 집어넣고 출력한다.

# 2. 힙을 2개를 사용하여 구현하기