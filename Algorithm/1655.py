# 링크드리스트 구현
class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next
    
def add(data):
  node = head
  while node.next:
    if node.next.data < data:
      node = node.next
    else: break
  newNode = Node(data)
  newNode.next = node.next
  node.next = newNode

  

N = int(input())
first = int(input())
head = Node(first)
print(head.data)
for i in range(1, N):
  temp = int(input())
  add(temp)
  mid_index = i // 2
  node = head
  for _ in range(mid_index):
    node = node.next
  print(node.data)
   
