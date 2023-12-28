N, L = map(int, input().split())

poolLength = [list(map(int, input().split()))for _ in range(N)]
poolLength.sort()
count = 0
for i in range(len(poolLength)):
  start, last = 0, 1
  tempLength = poolLength[i][last] - poolLength[i][start]
  # 판자 길이로 나눴을 때 나눠 떨어지는 경우
  if tempLength % L == 0:
     count += tempLength//L
  # 판자 길이로 나눠 떨어지지 않은 경우
  elif i+1 != N:
    sub = tempLength % L
    # 이전 판자가 다음 것을 커버 가능한 경우
    if poolLength[i][last] + L - sub >= poolLength[i+1][start]:
      poolLength[i+1][start] = poolLength[i][last] + L - sub
    # 이전 판자가 다음 것을 커버 불가능한 경우
    count += tempLength//L + 1
  else:
    count += tempLength//L+1
print(count)


###########################################################################
# 우선 각각의 웅덩이를 판자 길이로 나눴을 때 나누어 떨어지는지부터 검사했다.
# 나누어 떨어지는 경우 해당 나눗셈의 몫만큼 판자를 두면된다.

# 하지만 나누어떨어지지 않은 경우가 문젠데, 이 때는 2가지 경우를 생각할 수 있다.
# 1. 판자가 웅덩이 밖으로 삐져 나갈 때, 그 다음 웅덩이를 커버할 수 있다.
# 2. 판자가 웅덩이 밖으로 삐져 나갈 때, 그 다음 웅덩이를 커버할 수 없다.

# 만약 웅덩이를 커버할 수 있다면 해당 웅덩이의 last 값에다가 남은 판자의 길이 수를 더해서 그 다음 웅덩이의 시작 값으로 바꿔줬다.

# 한 가지 걸리는 점은, elif에서 저렇게 index range out을 방지했는데, 다른 방법이 있을까..?