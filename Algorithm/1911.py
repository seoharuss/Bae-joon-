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