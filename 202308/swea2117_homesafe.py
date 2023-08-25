for t in range(int(input())):
    N, M = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    res = []
    for x in range(N):
        for y in range(N):
            k = 1
            while k <= N+1:
                cost = k**2 + (k-1)**2
                cnt = 0
                for dx in range(-k+1, k):
                    for dy in range(-k+1, k):
                        if abs(dx) + abs(dy) <= k-1:
                            nx, ny = x+dx, y+dy
                            if 0 <= nx < N and 0 <= ny < N:
                                if MAP[nx][ny] == 1:
                                    cnt += 1
                if cnt*M - cost >= 0:
                    res.append(cnt)
                    k += 1
                else:
                    k += 1

    print(f'#{t+1} {max(res)}')
