T = int(input())

for t in range(1, T + 1):
    N = int(input())
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    arr = [[0]*N for _ in range(N)]

    arr[0] = list(range(1, N+1))
    numbers = list(range(1, N))

    pairs = []
    for num in numbers:
        pairs.append(num)
        pairs.append(num)

    for i in pairs:
        for j in range(i):
            arr[]


    print(f'#{t}')