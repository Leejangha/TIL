for t in range(int(input())):
    lst, N = map(int, input().split())
    numbers = []
    for l in str(lst):
        numbers.append(int(l))
    n = len(numbers)
    i = N
    while i > 0:
        for j in range(n-1):
            if i == 0:
                break
            MAX = max(numbers[j+1:])
            if numbers[j] < MAX:
                for k in range(n-1, j, -1):
                    if numbers[k] == numbers[k-1] == MAX and i > 1:
                        numbers[j], numbers[k-1] = numbers[k-1], numbers[j]
                        i -= 1
                        break
                    else:
                        if numbers[k] == MAX:
                            numbers[j], numbers[k] = numbers[k], numbers[j]
                            i -= 1
                            break
            else:
                if i % 2 == 0:
                    continue
                else:
                    if numbers.count(numbers[-2]) > 1:
                        continue
                    else:
                        numbers[-2], numbers[-1] = numbers[-1], numbers[-2]
        i -= 1
    res = ''.join(map(str, numbers))
    print(f'#{t+1} {res}')
