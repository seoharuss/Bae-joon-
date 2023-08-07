list = []

for i in range(5):
  count = 0
  a = int(input())
  for j in range(len(list)):
    if list[j] == a:
      list.remove(list[j])
      count += 1
      break
  if count == 0:
    list.append(a)

print(list[0])
