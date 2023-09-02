# 팩토리얼 풀이
def factorial(n):
  first = 1
  for i in range(n):
    first *= (i+1)
  return first

test_case = int(input())
for _ in range(test_case):
  west_site, east_site = map(int, input().split())
  print(factorial(east_site) // (factorial(east_site - west_site) * factorial(west_site)))



# 다이나믹 프로그래밍 풀이
import sys
input = sys.stdin.readline

# 다리는 겹치면 안된다.
def bridge(n,m):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1,m+1):
        dp[1][i] = i

    for j in range(2,n+1):
        for k in range(j,m+1):
            for l in range(k,j-1,-1):
                dp[j][k] += dp[j-1][l-1]

    return dp[n][m]

T = int(input().rstrip())
for _ in range(T):          
    n, m = map(int,input().rstrip().rsplit())
    print(bridge(n,m))
