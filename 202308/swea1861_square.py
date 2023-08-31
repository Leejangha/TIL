import sys
sys.setrecursionlimit(10**6)

delta = [(0,1), (1,0), (0,-1), (-1,0)]


def sequence(x, y, cnt, visited, start):
    global max_num, res
    visited[x][y] = 1
    for dx, dy in delta:
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < N:
            if MAP[nx][ny] - MAP[x][y] == 1:
                cnt += 1
                sequence(nx, ny, cnt, visited, start)
    if cnt >= max_num:
        max_num = cnt
        if max_num not in DICT:
            DICT[max_num] = MAP[start[0]][start[1]]
        if DICT[max_num] > MAP[start[0]][start[1]]:
            DICT[max_num] = MAP[start[0]][start[1]]


for t in range(int(input())):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    max_num = 0
    res = float('inf')
    visited = [[0]*N for _ in range(N)]
    DICT = {}
    for x in range(N):
        for y in range(N):
            if not visited[x][y]:
                start = (x, y)
                sequence(x, y, 1, visited, start)
    res = DICT[max_num]
    print(f'#{t+1} {res} {max_num}')
