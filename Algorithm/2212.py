N = int(input())
K = int(input())
sensor = list(map(int, input().split()))

sensor.sort()

array = []
for i in range(0, N-1):
  array.append(sensor[i+1] - sensor[i])

array.sort()

print(sum(array[:N-K]))