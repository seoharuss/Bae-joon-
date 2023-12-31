n = int(input())
bulb = list(map(int, input()))
target = list(map(int, input()))


def change(A, B):
    L = A[:]
    press = 0
    for i in range(1, n):
        # 이전 전구가 같은 상태면 pass
        if L[i-1] == B[i-1]:
            continue
        # 상태가 다를 경우
        press += 1
        for j in range(i-1, i+2):
            if j<n:
                L[j] = 1 - L[j]
    return press if L == B else 1e9


# 첫번째 전구의 스위치를 누르지 않는 경우
res = change(bulb, target)
# 첫번째 전구의 스위치를 누르는 경우
bulb[0] = 1 - bulb[0]
bulb[1] = 1 - bulb[1]
res = min(res, change(bulb, target) + 1)
print(res if res != 1e9 else -1)

###########################################
# 코드 완성은 못했지만 풀이방법은 알고 있어 적어보자면
# 현재 i번째 스위치를 눌러야 하는 상황이라면 이전의 i-1번째가 목표값과 같은지 비교해서
# 같으면 i번째 스위치를 누르지 않고, 다르다면 스위치를 눌러야 한다.

# 그다음 i+1번째 스위치를 눌러야하는지 결정할 때 i-1번째 전구는 신경안쓰므로 하나씩 for문을 돌아
# 스위치를 눌러야하는지 고민해야 한다.
