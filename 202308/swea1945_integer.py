T = int(input())

for t in range(1, T+1):
    N = int(input())
    ex = []
    numbers = [2, 3, 5, 7, 11]
    for num in numbers:
        count = 0
        while N % num == 0:
            count += 1
            N //= num
        ex.append(count)
    print(f'#{t}', *ex)