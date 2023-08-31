for t in range(int(input())):
    N, M = map(int, input().split())
    weights = list(map(int, input().split()))
    weights.sort()
    tones = list(map(int, input().split()))
    res = 0
    for tone in tones:
        for i in range(N-1, -1, -1):
            if tone >= weights[i]:
                res += weights[i]
                weights[i] = 51
                break
    print(f'#{t+1} {res}')
