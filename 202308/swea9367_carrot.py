T = int(input())

for t in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))
    cnt = 1
    res = []
    for i in range(1, N):
        if C[i] > C[i-1]:
            cnt += 1
        else:
            res.append(cnt)
            cnt = 1
    res.append(cnt)
    print(f'#{t} {max(res)}')
