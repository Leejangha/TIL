delta = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
 
 
def motion(turn, x, y):
    if turn == 'U':
        MAP[x][y], (dx, dy) = '^', delta['^']
    elif turn == 'D':
        MAP[x][y], (dx, dy) = 'v', delta['v']
    elif turn == 'L':
        MAP[x][y], (dx, dy) = '<', delta['<']
    elif turn == 'R':
        MAP[x][y], (dx, dy) = '>', delta['>']
    else:
        (dx, dy) = delta[MAP[x][y]]
    battle(turn, dx, dy)
 
 
def battle(turn, dx, dy):
    global nowx, nowy
    if turn == 'S':
        for k in range(1, 20):
            nx, ny = nowx + dx * k, nowy + dy * k
            if 0 <= nx < H and 0 <= ny < W:
                if MAP[nx][ny] == '*':
                    MAP[nx][ny] = '.'
                    break
                elif MAP[nx][ny] == '#':
                    break
    else:
        nx, ny = nowx + dx, nowy + dy
        if 0 <= nx < H and 0 <= ny < W:
            if MAP[nx][ny] == '.':
                MAP[nowx][nowy], MAP[nx][ny] = MAP[nx][ny], MAP[nowx][nowy]
                nowx, nowy = nx, ny
 
 
for t in range(int(input())):
    H, W = map(int, input().split())
    MAP = [list(input()) for _ in range(H)]
    N = int(input())
    lst = input()
    for x in range(H):
        for y in range(W):
            if MAP[x][y] in delta.keys():
                nowx, nowy = x, y
 
    for l in lst:
        motion(l, nowx, nowy)
 
    print(f'#{t + 1} ', end='')
    for M in MAP:
        print(''.join(M), end='\n')