N, K = map(int, input().split())
items = []


for i in range(N):
  w, v = map(int, input().split())
  items.append((w, v))

dp = [0 for _ in range(K+1)]




#################################################
# 첫번째 생각 (그리디 알고리즘)
# 알고리즘 수업때 배웠었던 개념을 그대로 적용하려고 해봄
# fractional knapsack

# 두번째 생각 (dp)
