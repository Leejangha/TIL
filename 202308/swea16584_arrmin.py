def f(i, N, sum_val):
    global min_val

    if sum_val > min_val:
        return

    elif i == N:
        if sum_val < min_val:
            min_val = sum_val
        return

    else:
        for j in range(i,N):
            A[i], A[j] = A[j], A[i]
            f(i+1,N,sum_val + arr[i][A[i]])
            A[i], A[j] = A[j], A[i]

for t in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    A = list(range(N))
    min_val = 9 * N
    f(0, N, 0)

    print(f'#{t+1} {min_val}')
