T = int(input())
 
for t in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    counts = []
 
    for i in range(N):
        count = 0
        for j in range(i, N):
            if numbers[i] > numbers[j]:
                count += 1
            counts.append(count)
    print(f'#{t+1} {max(counts)}')