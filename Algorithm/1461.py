# 책의 개수 N, 한 번에 들 수 있는 책의 개수 M
# N개의 책의 위치 주어짐

N, M = map(int, input().split())
location = list(map(int, input().split()))

positive = []
negative = []
temp = 0
for i in range(N):
  if location[i] < 0:
    negative.append(location[i])
  else:
    positive.append(location[i])
  if abs(location[i]) > temp:
    temp = abs(location[i])
    
negative.sort()
positive.sort(reverse=True)

result = 0
for i in range(0, len(negative), M):
  if -negative[i] != temp:
    result += (-negative[i])*2
for k in range(0, len(positive), M):
  if positive[k] != temp:
    result += positive[k]*2

if temp < 0:
  result += -temp
else:
  result += temp
print(result)