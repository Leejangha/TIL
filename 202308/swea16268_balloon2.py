T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    max_val = 0

    for i in range(N):
        for j in range(M):
            s = arr[i][j]
            d = s
            for k in range(4):
                ni ,nj = i+di[k], j+dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    s += arr[ni][nj]
            if max_val < s:
                max_val = s

    print(f'#{t} {max_val}')


# 수정
d = [(0,1), (1,0), (0,-1), (-1,0)]
 
for t in range(int(input())):
    N, M = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    max_val = 0
    for x in range(N):
        for y in range(M):
            ball = MAP[x][y]
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M:
                    ball += MAP[nx][ny]
            if ball > max_val:
                max_val = ball
    print(f'#{t+1} {max_val}')