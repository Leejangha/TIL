for t in range(int(input())):
    N, M = map(int, input().split())
    MAP = [list(input()) for _ in range(N)]
    dis = [[0]*M for _ in range(N)]
    Water = []
    Land = []
    for x in range(N):
        for y in range(M):
            if MAP[x][y] == 'W':
                Water.append((x,y))
            else:
                Land.append((x,y))
    for land in Land:
        lx, ly = land
        for water in Water:
            wx, wy = water
            d = abs(wx-lx) + abs(wy-ly)
            if dis[lx][ly] > d or dis[lx][ly] == 0:
                dis[lx][ly] = d
            if d == 1:
                break
    res = 0
    for d in dis:
        res += sum(d)
    print(f'#{t + 1} {res}')
