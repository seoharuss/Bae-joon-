from sys import stdin, maxsize

read = stdin.readline

n = int(read())
m = int(read())

graph = [[maxsize] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    s, e, w = map(int, read().split())
    if graph[s][e] > w:
        graph[s][e] = w


def floyd():
    for cross in range(1, n + 1):
        for s in range(1, n + 1):
            if cross == s:
                continue
            for e in range(1, n + 1):
                if cross == e or s == e:
                    continue

                if graph[s][e] > graph[s][cross] + graph[cross][e]:
                    graph[s][e] = graph[s][cross] + graph[cross][e]


floyd()
for s in range(1, n + 1):
    for e in range(1, n + 1):
        if graph[s][e] == maxsize:
            print(0, end=" ")
        else:
            print(graph[s][e], end=" ")
    print()

# #입력
# n = int(input())
# m = int(input())
# bus_cost = [[100001 for _ in range(n+1)] for _ in range(n+1)]

# for _ in range(m):
#     start, end, cost = map(int, input().split())
#     bus_cost[start][end] = min(cost, bus_cost[start][end])

# #플로이드-워셜 알고리즘
# for k in range(1, n+1): #경로 for문이 가장 상위 단계여야 누락되지 않는다
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if i == j: #자기 자신으로 오는 경우는 없다고 했으므로
#                 bus_cost[i][j] = 0 
#             else: #경로 거치는 것 or 직접 가는 것 or 이전 경로들
#                 bus_cost[i][j] = min(bus_cost[i][j],
#                                      bus_cost[i][k] + bus_cost[k][j])


# #출력
# for row in bus_cost[1:]:
#     for col in row[1:]:
#         if col == 100001:
#             print(0, end = " ")
#         else:
#             print(col, end = " ")
#     print()

##############################################################
# 플로이드-워셜 알고리즘
# 모든 최단 경로를 구하는 알고리즘
# 한 번 실행하여 모든 노드 간 최단 경로를 구할 수 있음

# 플로이도-워셜 알고리즘은 다익스트라 알고리즘과는 다르게 음의 간선도 사용 가능
