def bfs(maze):
  # 경로 개수를 세는 변수 
  count = 1
  visited = [[0]*M for _ in range(N)]
  visited[0][0] = 1
  queue = [(0, 0)]
  # 미로 탐색 가능 방향
  dx = [0, 0, -1, 1]
  dy = [-1, 1, 0, 0]
  while queue:
      count += 1
      # enqueue된 개수만큼 반복
      for _ in range(len(queue)):
          # 자료구조 queue이므로 선입 선출 방식으로 탐색
          x, y = queue.pop(0)
          for i in range(4):
              nx = x + dx[i]
              ny = y + dy[i]
              if nx == N-1 and ny == M-1:
                  return count
              if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1 and visited[nx][ny] == 0:
                  queue.append((nx, ny))
                  visited[nx][ny] = 1
  return count
    
      
N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

print(bfs(maze))

#####################################
# dfs의 장점
# 재귀적인 특징, 백트래킹을 이용하여 모든 경우를 하나씩 전부 탐색하는 경우, 그래프의 크기가 큰 경우
# optimal한 값을 찾는 것이 아닌 경우
# 경로의 특징을 저장해야 하는 경우 ex) 경로의 가중치, 이동과정에서의 제약

# bfs의 장점
# 최단거리, 최단 횟수 구하는 경우
# optimal한 답은 찾는 경우, BFS는 가장 처음 발견되는 해답이 최단 거리 !
# 탐색의 횟수를 구해야 하는 경우 

# bfs에 대해 더 탐구 