T = int(input())

for t in range(1, T+1):
    N = int(input())
    cnt = 0

    for i in range(1, N):
        for j in range(1, N):
            if i**2 + j**2 <= N**2:
                cnt += 1
    result = (cnt+N)*4 + 1
    print(f'#{t} {result}')