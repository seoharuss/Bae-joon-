N = int(input())

count_left = 0
count_right = 0
trophy = []
for i in range(N):
  put = int(input())
  trophy.append(put)

tall = 0
for j in range(N):
  if trophy[j] > tall:
    tall = trophy[j]
    count_left += 1

tall = 0
for k in reversed(range(N)):
  if trophy[k] > tall:
    tall = trophy[k]
    count_right += 1

print(count_left)
print(count_right)
