T = int(input())

for t in range(1, T + 1):
    N = int(input())
    di = [1, 0, -1, 0]
    dj = [0, -1, 0, 1]
    arr = [[0]*N for _ in range(N)]

    arr[0] = list(range(1, N+1))

    i = 0
    j = N - 1
    cnt = 0

    for num in range(N+1, N**2+1):
        i += di[cnt]
        j += dj[cnt]
        if 0 <= i < N and 0 <= j < N and arr[i][j] == 0:
            arr[i][j] = num
        else:
            i -= di[cnt]
            j -= dj[cnt]
            cnt += 1
            if cnt == 4:
                cnt = 0
            i += di[cnt]
            j += dj[cnt]
            arr[i][j] = num

    print(f'#{t}')
    for i in arr:
        print(*i)


# 방향 배열
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for t in range(1, int(input())+ 1):
    N = int(input())
    MAP = [[0] * N for _ in range(N)]
    
    i, j, number, direct = 0, 0, 1, 0
    
    MAP[i][j] = number
    number += 1
    
    while number <= N * N:
        ni = i + dx[direct]
        nj = j + dy[direct]

        if 0 <= ni < N and 0 <= nj < N and MAP[ni][nj] == 0:
            # 맵안에 존재하면서, 갈 수 있는 경우만
            i = ni
            j = nj
            MAP[i][j] = number
            number += 1
        else:
            direct = (direct + 1) % 4
            # 방향에서 들어갈 수 있는 조합 4가지

    print(f'#{t}')
    # 1
    # for i in range(N):
    #     for j in range(N):
    #         print(MAP[i][j], end = " ")
    #     print()

    # 2
    # for i in range(N):
    #     print(*MAP[i])

    # 3
    # for M in MAP:
    #     print(*M)