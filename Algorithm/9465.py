testCase = int(input())

for _ in range(testCase):
  n = int(input())
  score = [list(map(int, input().split())) for _ in range(2)]
  
  dp = [[0 for _ in range(n)] for _ in range(2)]
  dp[0][0] = score[0][0]
  dp[1][0] = score[1][0]
  
  if n == 1:
    print(max(dp[0][0], dp[1][0]))
    continue
  dp[0][1] = dp[1][0] + score[0][1]
  dp[1][1] = dp[0][0] + score[1][1]
  
  if n == 2:
    print(max(dp[0][1], dp[1][1]))
    continue
  
  for i in range(2, n):
    dp[0][i] = max(dp[1][i-1]+score[0][i], dp[1][i-2]+score[0][i])
    dp[1][i] = max(dp[0][i-1]+score[1][i], dp[0][i-2]+score[1][i])
  print(max(dp[0][i], dp[1][i]))
  
  
################################################################
# 내가 생각한 풀이
# 각각의 열에서 값이 큰 것을 고르되, 행을 번갈아 가며 다음꺼에서는 다른 행의 값을 선택한다.
# 하지만 예를들어 0행 k열과 1행 k+1열을 더한 것보다 0행 k+1열의 값이 더 클 수도 있으므로 비교해서 더 큰 값을 dp에 넣는다.

# dp를 2차원 배열로 사용해야 한다...?

# 내가 생각했던 방법은 맞았지만 dp를 1차원 리스트가 아닌 2차원 리스트로 했어야 했다.

# 코드 수정은 금방 끝냄