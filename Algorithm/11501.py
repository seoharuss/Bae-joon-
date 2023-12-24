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
  