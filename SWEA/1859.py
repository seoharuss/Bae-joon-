MAX = 1000001
arr = [0] * MAX

test_case = int(input())

for i in range(test_case):
  day = int(input())
  result = 0
  arr[:day] = map(int, input().split())
  tmp = arr[day - 1]
  for k in range(day-1, -1, -1):
    if tmp > arr[k]:
      result += tmp - arr[k]
    else:
      tmp = arr[k]
  print(f"#{i+1} {result}")
