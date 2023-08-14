a = list(map(str, input()))
count = 0

for i in range(len(a)-1,-1, -1):
  count += 1
  if i == 0:
    break
  if a[i] == '=':
    if a[i-1] == 'c':
      count -= 1
    elif a[i-1] == 'z':
      if a[i-2] == 'd':
        count -= 1
      count -= 1
    elif a[i-1] == 's':
      count -= 1
  elif a[i] == '-':
    if a[i-1] == 'c':
      count -= 1
    elif a[i-1] == 'd':
      count -= 1
  elif a[i] == 'j':
    if a[i-1] == 'l':
      count -= 1
    elif a[i-1] == 'n':
      count -= 1
    
print(count)
#########################################
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
print(len(word))
