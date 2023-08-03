T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    spsort = []

    for i in range(5):
        spsort.append(arr[N-1-i])
        spsort.append(arr[i])

    print(f'#{t}', *spsort)