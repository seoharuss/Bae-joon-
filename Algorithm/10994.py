def draw_star(n,idx):
    if n==1:
        stars[idx][idx] = '*'
        return
    count = 4*n-3

    for i in range(idx,count+idx):
        # 위쪽 가로열 직선
        stars[idx][i]='*'
        # 아래쪽 가로열 직선
        stars[idx+count-1][i]='*'
        # 위쪽 세로행 직선
        stars[i][idx]='*'
        # 아래쪽 세로행 직선
        stars[i][idx+count-1]='*'
    # 시작점이 (0,0)에서 (2,2)로 변경되었다고 think
    return draw_star(n-1,idx+2)

n = int(input()) # n을 입력받는다.
star_count = 4*n -3

stars = [[' ']*star_count for _ in range(star_count) ]

# (0,0)부터 시작
draw_star(n,0)

for i in range(star_count):
    for j in range(star_count):
        print(stars[i][j],end="")
    print()
