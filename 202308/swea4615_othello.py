delta = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
B = 1
W = 2
color = [0,2,1]


def play(x, y, c, N):
    MAP[x][y] = c
    for dx, dy in delta:
        nx, ny = x+dx, y+dy
        C = []
        while 0 <= nx < N and 0 <= ny < N and MAP[nx][ny] == color[c]:
            C.append((nx,ny))
            nx, ny = nx+dx, ny+dy
        if 0 <= nx < N and 0 <= ny < N and MAP[nx][ny] == c:
            for i, j in C:
                MAP[i][j] = c


for t in range(int(input())):
    N, M = map(int, input().split())
    turn = [list(map(int, input().split())) for _ in range(M)]
    MAP = [[0]*N for _ in range(N)]
    n = N//2
    MAP[n-1][n-1], MAP[n][n] = W, W
    MAP[n][n-1], MAP[n-1][n] = B, B
    for y, x, c in turn:
        play(x-1, y-1, c, N)

    b = 0
    w = 0
    for x in range(N):
        for y in range(N):
            if MAP[x][y] == B:
                b += 1
            elif MAP[x][y] == W:
                w += 1
    print(f'#{t+1} {b} {w}')
