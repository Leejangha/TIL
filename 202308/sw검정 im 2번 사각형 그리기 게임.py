d = [(-1,0), (0,-1)]

for t in range(int(input())):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for x in range(N):
        for y in range(N):
            num = MAP[x][y]
            max_s = 0
            for i in range(N, N-x, -1):
                for j in range(N, N-y, -1):
                    s = 0
                    for di, dj in d:
                        ni, nj = i+di, j+di
                        if x <= ni <N and y <= nj < N and MAP[ni][nj] == num:
                            s = (ni-x)*(nj-y)
                            if s == max_s:
                                cnt += 1
                            elif s > max_s:
                                max_s = s
                                cnt = 0
                            else:
                                break
                            print(max_s)

    print(f'#{t+1} {cnt}')
