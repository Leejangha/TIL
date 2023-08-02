T = int(input())

for t in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    di = [-1,0,1,0]
    dj = [0,1,0,-1]

    max_val = 0
    for i in range(N):

        for j in range(M):
            s = arr[i][j]
            d = s
            for k in range(4):
                for r in range(1, d+1):
                    ni, nj = i+di[k]*r, j+dj[k]*r
                    if 0 <= ni < N and 0 <= nj < M:
                        s += arr[ni][nj]
            if max_val < s:
                max_val = s
    print(f'#{t} {max_val}')