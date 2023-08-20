d = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]

for t in range(int(input())):
    N = int(input())
    MAP = [input() for _ in range(N)]
    res = 'NO'
    for x in range(N):
        for y in range(N):
            if MAP[x][y] == 'o':
                for dx, dy in d:
                    cnt = 1
                    for k in range(1, 5):
                        nx, ny = x+dx*k, y+dy*k
                        if 0 <= nx < N and 0 <= ny < N:
                                if MAP[nx][ny] == 'o':
                                    cnt += 1
                    if cnt == 5:
                        res = 'YES'
    print(f'#{t+1} {res}')
