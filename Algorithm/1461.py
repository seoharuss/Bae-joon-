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

########################################3
# 풀이방법
# 일단 양수와 음수가 정점을 기준으로 나뉘어 있기에 양수와 음수를 따로 리스트에 구분해준다.
# 그리고 가장 먼 지점은 갔다가 안돌아와도 되기에 마지막에 놓는 것으로 하고 따로 temp변수에 저장해둔다.
# 그리고 양수와 음수 리스트를 정렬해주고, 책을 한번에 M개를 들 수 있기에 FOR 반복문을 M씩 증가하면 반복한다.
# 가장 먼 거리를 제외한 나머지를 왔다갔다 하므로 *2를 해주고 마지막에 가장 먼거리를 더해주기만 하면 된다.
