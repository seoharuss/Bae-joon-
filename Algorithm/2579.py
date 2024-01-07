stairCount = int(input())
stairPoint = []

for i in range(stairCount):
  stairPoint.append(int(input()))

dp = [0]*stairCount
dp[0] = stairPoint[0]
dp[1] = stairPoint[0]+stairPoint[1]
dp[2] = max(dp[0]+stairPoint[2], stairPoint[1]+stairPoint[2])

for i in range(3, stairCount):
  dp[i] = max(dp[i-2]+stairPoint[i], dp[i-3]+stairPoint[i-1]+stairPoint[i])

print(dp[stairCount-1])
