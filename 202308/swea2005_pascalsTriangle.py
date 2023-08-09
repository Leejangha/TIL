T = int(input())

for t in range(1, T+1):
    N = int(input())
    f = [[0]*N for _ in range(N)]
    f[0][0] = 1
    for i in range(1, N):
        for j in range(i+1):
            f[i][j] = f[i-1][j-1] + f[i-1][j]
        while 0 in f[i-1]:
            f[i-1].remove(0)

    print(f'#{t}')
    for i in range(N):
        print(*f[i])
