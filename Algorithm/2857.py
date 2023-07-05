s_list = [input() for _ in range(5)]
wrong = 0
for j in range(5):
  if s_list[j].find('FBI') == -1:
    wrong += 1
  else:
    print(j+1, end = " ")
if wrong == 5:
  print("HE GOT AWAY!")
