def fish(m, g, k):
    q = []
    t = 0
    if 0 in arrival:
        return 'Impossible'
    while t < g:
        t += 1
        if t % m == 0:
            q.append(k)
        if t in arrival:
            if q:
                q[0] -= 1
                if q[0] == 0:
                    q.pop(0)
            else:
                return 'Impossible'
    return 'Possible'


for tc in range(int(input())):
    N, M, K = map(int, input().split())
    arrival = sorted(list(map(int, input().split())))
    last = arrival[-1]
    res = fish(M, last, K)

    print(f'#{tc+1} {res}')
