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
# x축엔 가방 1~k까지 무게, y축은 물건 N개 개수 만큼의 배열을 만든다
# 현재 물건이 현재 돌고있느 무게보다 작다면 바로 [이전 물건][같은 무게]를 입력
# 현재 물건을 넣어준다. 물건을 넣은 뒤의 남은 무게를 채울 수 있는 최댓값을 위의 행에서 가져와 더해준다.
# 현재 물건을 넣어주는 것보다 다른 물건들로 채우는 값을 가져온다.
# 더 큰 값을 dp에 저장해준다. 이 값은 현재까지의 물건들로 구성할 수 있는 가장 가치 높은 구성이다.
