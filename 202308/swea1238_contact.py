d = [(0,1), (1,0), (0,-1), (-1,0)]


def bfs(stx, sty, n):
    visited = [[0]*n for _ in range(n)]
    q = []
    q.append((stx,sty))
    visited[stx][sty] = 1
    while q:
        x, y = q.pop(0)
        if maze[x][y] == 3:
            return 1
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] != 1 and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = 1
    return 0


for t in range(10):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    phones = [[]*(N+1) for _ in range(N+1)]
    for i in range(0, N, 2):
        v1 = lst[i//2]
        v2 = lst[i//2+1]
        phones[v1].append(v2)
    print(phones)

    res = bfs(x, y, N)
    print(f'#{t+1} {res}')
