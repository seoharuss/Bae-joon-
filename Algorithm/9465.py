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
  
################################################################
# 내가 생각한 풀이
# 각각의 열에서 값이 큰 것을 고르되, 행을 번갈아 가며 다음꺼에서는 다른 행의 값을 선택한다.
# 하지만 예를들어 0행 k열과 1행 k+1열을 더한 것보다 0행 k+1열의 값이 더 클 수도 있으므로 비교해서 더 큰 값을 dp에 넣는다.
