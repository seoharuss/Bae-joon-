S = list(input())
T = list(input())

result = 0
while T:
  if T[-1] == 'A':
    T.pop()
  elif T[-1] == 'B':
    T.pop()
    T.reverse()
  if S == T:
    result = 1
    break
print(result)

# 1차 제출 : 메모리 초과
# 2차 생각 : 역으로 생각하기 
# 문자열 뒤에 A를 추가한다 -> 문자열 마지막에 A가 나오면 A를 삭제한다.
# 문자열을 뒤집고 뒤에 B를 추가한다 -> 문자열을 뒤집고 뒤에 B가 나오면 B를 삭제한다.

# S를 T로 만들 생각만 계속 했는데, 생각을 역으로 발상하는 것도 해봐야겠다고 생각했다.
# 이 문제의 핵심은 T를 S로 바꾸는 것이 핵심이다.