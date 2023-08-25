for t in range(int(input())):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N+1)]
    h = []
    for i in range(N+1):
        for j in range(N+1):
            if MAP[i][j] == 2:
                x, y = i, j
            elif MAP[i][j] == 1:
                h.append((i,j))
    D = 0
    R = 0
    for hx, hy in h:
        D = ((hx-x)**2 + (hy-y)**2)**0.5
        if D > R:
            if D.is_integer():
                R = int(D)
            else:
                R = int(D)+1
    print(f'#{t+1} {R}')
