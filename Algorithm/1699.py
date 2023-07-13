# N보다 작거나 같은 제곱수들의 합으로 표현가능
# 제곱수 항의 최소 개수 구하기

number = int(input())
dp = [i for i in range(number+1)]

for i in range(1, number + 1):
  for j in range(1, i):
    if j*j>i:
      break
    if dp[i] > dp[i-j*j]+1:
      dp[i] = dp[i-j*j]+1
print(dp[number])
