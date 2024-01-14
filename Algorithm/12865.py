N, K = map(int, input().split())
items = [[0,0]]
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for _ in range(N):
  items.append(list(map(int, input().split())))
  
for i in range(1, N+1):
  for j in range(1, K+1):
    weight = items[i][0]
    value = items[i][1]
    if j < weight:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j])
print(dp[N][K])
#################################################
# 첫번째 생각 (그리디 알고리즘)
# 알고리즘 수업때 배웠었던 개념을 그대로 적용하려고 해봄
# fractional knapsack

# 두번째 생각 (dp)
