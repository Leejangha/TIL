for t in range(int(input())):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    idx = list(range(N))
    j = N
    while idx.count(0) < (N-1):
        for i in range(N):
            if idx.count(0) == (N-1):
                break
            Ci[i] //= 2
            if Ci[i] == 0:
                if j < M:
                    Ci[i] = Ci[j]
                    idx[i] = j
                    j += 1
                else:
                    idx[i] = 0

    res = max(idx) + 1
    print(f'#{t+1} {res}')
