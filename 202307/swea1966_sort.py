T = int(input())
 
for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    for i in range(N):
        for j in range(N):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    print(f'#{t}', end = " ")
    for i in range(N):
        print(numbers[i], end = " ")
    print()