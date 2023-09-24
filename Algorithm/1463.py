import queue

x = int(input())
visit = [0] * (x+1)
repo = queue.Queue()
repo.put(x)

while repo:
  temp = repo.get()
  if temp == 1: break
  if temp % 3 == 0 and visit[temp//3] == 0:
    repo.put(temp//3)
    visit[temp//3] = visit[temp]+1
  if temp % 2 == 0 and visit[temp//2] == 0:
    repo.put(temp//2)
    visit[temp//2] = visit[temp]+1
  if visit[temp-1] == 0:
    repo.put(temp-1)
    visit[temp-1] = visit[temp]+1

print(visit[1])
