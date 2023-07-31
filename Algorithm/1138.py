N = int(input())

a = list(map(int, input().split()))
result_list = [0]*N
for i in range(N):
  cnt = 0
  for j in range(N):
    if cnt == a[i] and result_list[j] == 0:
      result_list[j] = i+1
      break
    elif result_list[j] != 0:
      continue
    else:
      cnt += 1
      
print(' '.join(map(str,result_list)))
