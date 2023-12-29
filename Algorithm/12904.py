from collections import deque

def reverse(string):
  reversed_string = string[::-1]
  return reversed_string

S = input()
T = input()

queue = deque([S])
count = 1
while len(queue[0]) != len(T):
  temp = queue.popleft()
  first = temp+'A'
  second = reverse(temp)+'B'
  queue.append(first)
  queue.append(second)
  count += 1

result = 0
for i in queue:
  if T == i:
    result = 1
print(result)