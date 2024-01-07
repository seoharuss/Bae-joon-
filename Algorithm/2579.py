stairCount = int(input())
stairPoint = [0] * 301
for i in range(1, stairCount + 1):
    stairPoint[i] = int(input())

dp = [0]*301
dp[1] = stairPoint[1]
dp[2] = stairPoint[1]+stairPoint[2]
dp[3] = max(dp[1]+stairPoint[3], stairPoint[2]+stairPoint[3])

for i in range(4, stairCount+1):
  dp[i] = max(dp[i-2]+stairPoint[i], dp[i-3]+stairPoint[i-1]+stairPoint[i])

print(dp[stairCount])
