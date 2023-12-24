testCase = int(input())

for _ in range(testCase):
  days = int(input())
  price = list(map(int, input().split()))
  bestProfit = 0
  
  maxPrice = 0
  for i in range(days-1, -1, -1):
    # 만약 작은수를 만나면 파는 것
    if maxPrice > price[i]:
      bestProfit += maxPrice - price[i]
    # 만약 큰 수 만나면 업데이트
    elif maxPrice < price[i]:
      maxPrice = price[i]
  print(bestProfit)
  
##############################################
# 맨 처음에는 앞에서부터 판단을 하여 현재 값보다 그 뒤 값이 더 큰 경우는 팔지 않고, 작은 경우는 팔려고 코드를 구현했다.
# 결과값은 나왔지만 시간초과가 걸려 왜 틀렸는지 고민했다.

# 생각해보니까 그리디 알고리즘으로 풀면 되겠다고 생각하여 뒤에서 부터 판단하는 것으로 생각했다.
# 최댓수가 나오기전까지 가지고 있다가 나오면 팔고, 차액을 계산한다.
# 뒤에서부터 작은 수를 만날때마다 팔고, 큰 수 만나면 업데이트

