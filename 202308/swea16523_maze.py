d = [(0,1), (1,0), (0,-1), (-1,0)]


def checknode(x, y, N):
    if maze[x][y] == 3:
        return 1
    maze[x][y] = 1
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] != 1:
            if checknode(nx, ny, N):
                return 1
    return 0


for t in range(int(input())):
    N = int(input())
    maze = [list(map(int, *input().split())) for _ in range(N)]
    stack = []
    for x in range(N):
        for y in range(N):
            if maze[x][y] == 2:
                res = checknode(x, y, N)

    print(f'#{t+1} {res}')
