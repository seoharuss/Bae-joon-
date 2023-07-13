#연속 정답 가산점
#틀린 문제 0점
#채점 결과가 주어졌을 때, 총 점수 계산하는 프로그램

result_number = int(input())
result = list(map(int, input().split()))

sum = 0
multiple = 0
for i in range(len(result)):
  if result[i] == 1:
    multiple += 1
    sum += multiple
  else:
    multiple = 0
print(sum)
