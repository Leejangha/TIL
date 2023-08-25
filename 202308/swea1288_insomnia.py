for t in range(int(input())):
    N = int(input())
    numbers = list(range(10))
    k = 0
    while numbers:
        k += 1
        s = str(N*k)
        for char in s:
            if int(char) in numbers:
                numbers.remove(int(char))
    res = N*k

    print(f'#{t+1} {res}')
