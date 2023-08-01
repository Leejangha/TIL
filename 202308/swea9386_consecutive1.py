T = int(input())

for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input()))
    counts = []
    for i in range(N):
        if numbers[i] == 1:
            count = 0
            for j in range(N-i):
                if numbers[i+j] == 1:
                    count += 1
                else:
                    break
                counts.append(count)
    print(f'#{t} {max(counts)}')