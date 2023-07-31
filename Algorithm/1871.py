N = int(input())

for _ in range(N):
  alphabet, number = input().split('-')
  temp = int(number)
  alphabet_num = 0
  for i in range(3):
    alphabet_num += (ord(alphabet[i])-65)*26**(2-i)
    
  if abs(alphabet_num - temp) <= 100:
    print("nice")
  else:
    print("not nice")
