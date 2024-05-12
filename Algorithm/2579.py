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

#########################################################3
# dp로 접근하는 문제
# 연속3번 계단을 오르면 안되므로 max값을 계산할 때
# i-1번째에서 오는 값은 i-3의 값에서 i-1과 i를 더한다.
# i-2번째에서 오는 값은 해당 값에 현재 i를 더한다.
