cities = int(input())
bus = int(input())

graph = [[0 for _ in range(cities+1)] for _ in range(cities+1)]

# 행 = 시작, 열 = 도착, 행렬값 = 비용
for i in range(1, bus+1):
  start, finish, cost_temp = map(int, input().split())
  if graph[start][finish] == 0:
    graph[start][finish] = cost_temp
  else:
    graph[start][finish] = min(cost_temp, graph[start][finish])

for k in range(1, cities+1):
  for i in range(1, cities+1):
    for j in range(1, cities+1):
      graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
      
print(graph)

##############################################################
# 플로이드-워셜 알고리즘
# 모든 최단 경로를 구하는 알고리즘
# 한 번 실행하여 모든 노드 간 최단 경로를 구할 수 있음

# 플로이도-워셜 알고리즘은 다익스트라 알고리즘과는 다르게 음의 간선도 사용 가능
