for t in range(int(input())):
    N = float(input())
    Bin = ''
    res = True
    i = 1
    while res:
        if N - 0.5**i > 0:
            Bin += '1'
            N -= 0.5 ** i
        elif N - 0.5**i < 0:
            Bin += '0'
        else:
            Bin += '1'
            break
        i += 1
        if len(Bin) >= 13:
            res = False
    if res:
        print(f'#{t+1} {Bin}')
    else:
        print(f'#{t+1} overflow')
