T = int(input())

for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    max_idx = 0
    min_idx = 0
    for i in range(N):
        if numbers[i] >= numbers[max_idx]:
            max_idx = i
        if numbers[i] < numbers[min_idx]:
            min_idx = i
    print(f'#{t} {abs(max_idx - min_idx)}')