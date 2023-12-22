chain_count = int(input())
chain_length = list(map(int, input().split()))

dp =[]
chain_length.sort()
# 열고 닫아야할 최소한의 고리 수 = 오름차순으로 정렬한 후
# 인덱스가 작은 값 부터 열고 닫는 고리로 변환
# 갯수만큼 연결
chain_result = 0
for i in range(chain_count):
  chain_round = chain_length[i]
  # 만약 해당 체인을 다 풀어도 못 연결하는 경우
  if chain_round < chain_count-2:
    chain_count = chain_count-chain_length[i]-1
    chain_result += chain_length[i]
  # 만약 해당 체인을 다 풀기 전에 연결하는 경우
  if chain_round > chain_count-2:
    chain_result += chain_count-1
    break
  # 해당 체인을 다 풀면 연결이 딱 되는 경우
  if chain_round == chain_count-2:
    chain_result += chain_count-2
    break
print(chain_result)

####################################################
# 처음엔 정렬해서 풀어야겠다고 생각하지 못했다. 그냥 총 체인의 개수-2이면 연결될 줄 알았지만
# 여러가지 경우의 수를 생각하고, 정렬해서 가장 작은 길이의 체인을 분해해서 다른 체인을 연결하는 고리로 사용하면 되겠다고 생각했다.
# 그리디 알고리즘을 통해 가장 작은 체인의 길이부터 순서대로 분해하는 알고리즘을 사용했다.