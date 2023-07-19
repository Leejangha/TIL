T = int(input)

for i in range(T):
    N, M = list(map(int, input().split()))

    arr = list(map(int, input().split()) for _ in range(N))
    cross = []

    for j in range(M):
        cross.append(arr[j])
