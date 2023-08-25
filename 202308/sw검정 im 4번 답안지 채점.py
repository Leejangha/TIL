for t in range(int(input())):
    N, M = map(int, input().split())
    answer = list(map(int, input().split()))
    lst = [list(map(int, input().split())) for _ in range(N)]
    point = []
    for l in lst:
        cnt = 0
        bonus = 0
        for i in range(M):
            if l[i] == answer[i]:
                cnt += (1 + bonus)
                bonus += 1
            else:
                bonus = 0
        point.append(cnt)
    res = max(point) - min(point)

    print(f'#{t+1} {res}')
