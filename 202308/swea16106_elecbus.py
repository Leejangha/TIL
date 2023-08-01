T = int(input())

for t in range(1, T+1):
    K, N, M = map(int, input().split())
    lines = [0] * (N+1)
    num = list(map(int, input().split()))
    for i in num:
        lines[i] += 1
    count = 0
    i = 0
    while i < N:
        if (i + K) >= N:
            break
        found_station = False
        for j in range(K):
            if lines[i+K-j] == 1:
                count += 1
                i += K-j
                found_station = True
                break
        if not found_station:
            count = 0
            break
    print(f'#{t} {count}')