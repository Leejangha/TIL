T = 10

for t in range(1, T+1):
    N = int(input())
    boxs = list(map(int, input().split()))
    max_idx = 0
    min_idx = 0

    for i in range(N):
        max_idx = boxs.index(max(boxs))
        boxs[max_idx] -= 1
        min_idx = boxs.index(min(boxs))
        boxs[min_idx] += 1
        if (max(boxs) - min(boxs)) == 1:
            break

    print(f'#{t} {max(boxs) - min(boxs)}')