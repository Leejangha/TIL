for t in range(int(input())):

    N, K = map(int, input().split())
    Sample = list(map(int, input().split()))
    PassCode = list(map(int, input().split()))

    res = 1
    if PassCode[0] in Sample:
        now_idx = Sample.index(PassCode[0])
        cnt = 1
        for Pass in PassCode[1:]:
            next_idx = now_idx + 1
            lst = Sample[next_idx:]
            if Pass in lst:
                now_idx = lst.index(Pass) + next_idx
                cnt += 1
                if cnt == K:
                    break
            else:
                res = 0
                break
    else:
        res = 0

    print(f'#{t+1} {res}')
