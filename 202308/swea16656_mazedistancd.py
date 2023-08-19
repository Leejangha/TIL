def bfs(stx, sty, n):
    visited = [[0]*n for _ in range(n)]
    q = []
    q.append((stx,sty))
    visited[stx][sty] = 1
    while q:
        x, y = q.pop(0)
        if maze[x][y] == 3:
            return visited[x][y] - 2
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] != 1 and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1
    return 0

d = [(0,1),(1,0),(0,-1),(-1,0)]

for t in range(int(input())):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    start = [(x, y) for x in range(N) for y in range(N) if maze[x][y] == 2]
    x, y = start[0]
    res = bfs(x, y, N)
    print(f'#{t+1} {res}')
