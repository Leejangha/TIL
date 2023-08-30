def f(i, N):
    global p
    global min_e
    if i == N:
        lst = [1] + p + [1]
        e = 0
        for j in range(N+1):
            e += MAP[lst[j]-1][lst[j+1]-1]
        if min_e > e:
            min_e = e
        return
    else:
        for j in range(N):
            if used[j] == 0:
                p[i] = array[j]
                used[j] = 1
                f(i+1, N)
                used[j] = 0


for t in range(int(input())):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    array = list(range(2, N+1))
    used = [0] * (N-1)
    p = [0] * (N-1)
    min_e = float('inf')
    f(0, N-1)

    print(f'#{t+1} {min_e}')
