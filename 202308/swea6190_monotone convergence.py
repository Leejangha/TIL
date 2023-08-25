for t in range(int(input())):
    N = int(input())
    numbers = list(map(int, input().split()))
    monotone = []
    for i in range(N-1):
        for j in range(i+1,N):
            mul = str(numbers[i] * numbers[j])
            is_conver = True
            for k in range(len(mul)-1):
                if mul[k+1] < mul[k]:
                    is_conver = False
            if is_conver:
                monotone.append(int(mul))

    res = -1
    if monotone:
        res = max(monotone)

    print(f'#{t+1} {res}')
