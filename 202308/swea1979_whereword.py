T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = []

    for _ in range(N):
        arr.append(list(map(int, input().split())))
    r_arr = list(map(list, zip(*arr)))
    result = []

    def count_K(lst):
        count = 0
        for num in lst:
            if num == 1:
                count += 1
            else:
                if count > 0:
                    result.append(count)
                    count = 0
        if count > 0:
            result.append(count)

    for i in range(N):
        count_K(arr[i])
        count_K(r_arr[i])

    answer = result.count(K)
    print(f'#{t} {answer}')