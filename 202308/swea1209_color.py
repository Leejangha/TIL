T = int(input())

for t in range(1, T+1):
    N = int(input())
    area = [[0]*10 for _ in range(10)]
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        counts = 0
        for j in range(c1, c2 + 1):
            for k in range(r1, r2 + 1):
                if area[k][j] == 0 or area[k][j] != color and area[k][j] != 3:
                    area[k][j] += color
                else:
                    continue
        for j in range(10):
            counts += area[j].count(3)
    print(f'#{t} {counts}')