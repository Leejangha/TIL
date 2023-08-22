for t in range(int(input())):
    N, K = map(int, input().split())
    Sample = list(map(int, input().split()))
    PassCode = list(map(int, input().split()))

    res = 1
    now_idx = Sample.index(PassCode[0])
    for Pass in PassCode:
        next_idx = now_idx + 1
        if Pass in Sample[next_idx:]:
            now_idx = Sample[next_idx:].index(Pass) + next_idx
        else:
            res = 0
            break

    print(f'#{t+1} {res}')
