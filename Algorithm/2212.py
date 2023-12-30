N = int(input())
K = int(input())
sensor = list(map(int, input().split()))

sensor.sort()

array = []
for i in range(0, N-1):
  array.append(sensor[i+1] - sensor[i])

array.sort()

print(sum(array[:N-K]))

###########################################
# 음,,, 배열에 각 센서들의 거리 차를 더하고
# 해당 거리 차를 다시 오름차순으로 정렬해서
# 앞에서부터 n-k개를 더해준다는 것은 센서 간의 거리의 차가 가장 큰 값을 k-1개 빼주는 것과 같다고 볼 수 있다.
# 위의 문장이 핵심이다.

# 이처럼 해당 내용을 잘 이해해야 겠다고 생각한다.