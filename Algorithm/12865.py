N, K = map(int, input().split())
size = [0 for _ in range(N)]
value = [0 for _ in range(N)]


for i in range(N):
  size[i], value[i] = map(int, input().split())



#################################################
# 첫번째 생각 (그리디 알고리즘)
# 알고리즘 수업때 배웠었던 개념을 그대로 적용하려고 해봄
# fractional knapsack

# 두번째 생각 (dp)
