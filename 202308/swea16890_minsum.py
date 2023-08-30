for t in range(int(input())):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if x == 0 and y == 0:
                continue
            if x == 0:
                MAP[x][y] += MAP[x][y-1]
            elif y == 0:
                MAP[x][y] += MAP[x-1][y]
            else:
                MAP[x][y] += min(MAP[x-1][y], MAP[x][y-1])
    res = MAP[N-1][N-1]
    print(f'#{t+1} {res}')
