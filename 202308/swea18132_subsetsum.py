T = int(input())
A = list(range(1, 13))

for t in range(1, T+1):
    N, K = map(int,input().split())

    subsets = []
    result = 0
    for i in range(1<<12):
        arr = []
        for j in range(12):
            if i & (1<<j):
                arr.append(A[j])
        if len(arr) == N:
            subsets.append(arr)
    for subset in subsets:
        if sum(subset) == K:
            result += 1
    print(f'#{t} {result}')