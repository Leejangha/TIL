for t in range(int(input())):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    d = N//2
    x = y = d
    res = 0
    for dx in range(-d, d+1):
        for dy in range(-d, d+1):
            if abs(dx) + abs(dy) <= d:
                res += farm[x+dx][y+dy]
    print(f'#{t+1} {res}')
