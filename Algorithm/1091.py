card_count = int(input())
card_final = list(map(int, input().split()))
card_rule = list(map(int, input().split()))

copy = card_final

card_basic = [0, 1, 2]*(int(card_count / 3))

new_card_final = [0] * card_count
count = 0

while card_final != card_basic:
  for i in range(card_count):
    new_card_final[card_rule[i]] = card_final[i]
  
  card_final = new_card_final
  new_card_final = [0]*card_count
  count += 1
  
  if copy == card_final:
    count = -1
    break
print(count)
