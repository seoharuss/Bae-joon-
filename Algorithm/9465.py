testCase = int(input())

for _ in range(testCase):
  n = int(input())
  score = [list(map(int, input().split())) for _ in range(2)]
  print(score)