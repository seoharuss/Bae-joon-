houseCount = int(input())

rgb = [0]*houseCount
for i in range(houseCount):
  rgb[i] = list(map(int, input().split()))

# 1부터 시작하는 이유는 다음 입력값이 이전 입력값의 최소값을 사용하기 때문
for i in range(1, houseCount):
  rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2]) + rgb[i][0]
  rgb[i][1] = min(rgb[i-1][0], rgb[i-1][2]) + rgb[i][1]
  rgb[i][2] = min(rgb[i-1][0], rgb[i-1][1]) + rgb[i][2]

print(min(rgb[houseCount-1][0], rgb[houseCount-1][1], rgb[houseCount-1][2]))
