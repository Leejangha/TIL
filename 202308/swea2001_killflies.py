T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    max_val = 0
    for i in range(N):
        for j in range(N):
            s = arr[i][j]
            d = 0
            for k in range(M):
                for l in range(M):
                    ni , nj = i + k, j + l
                    if 0 <= ni < N and 0 <= nj < N:
                        d += arr[ni][nj]
            if max_val < d:
                max_val = d

    print(f'#{t} {max_val}')