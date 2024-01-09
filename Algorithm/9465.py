testCase = int(input())

for _ in range(testCase):
  n = int(input())
  score = [list(map(int, input().split())) for _ in range(2)]
  
  dp = [0 for _ in range(n)]
  temp = 0
  if score[0][0] > score[1][0]:
    dp[0] = score[0][0]
    temp = 1
  else:
    dp[0] = score[1][0]
    temp = 0
    
  for i in range(1, n-1):
    if score[temp][i]+score[not temp][i+1] < score[temp][i+1]:
      dp[i+1] = dp[i-1]+score[temp][i+1]
      temp = not temp
    else:
      dp[i] = dp[i-1]+score[temp][i]
      temp = not temp
  if dp[n-1] == 0:
    dp[n-1] = dp[n-2] + score[temp][n-1]
  print(dp[n-1])