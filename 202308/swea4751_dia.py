T = int(input())

for t in range(1, T+1):
    string = input()
    lst = [['.'] * (len(string) * 4 + 1) for _ in range(5)]
    N = len(lst[0])
    for i in range(5):
        if i in [0, 4]:
            for j in range(2, N, 4):
                lst[i][j] = '#'
        elif i in [1, 3]:
            for j in range(1, N, 2):
                lst[i][j] = '#'
        else:
            k = 0
            for j in range(0, N, 2):
                if j % 4 == 0:
                    lst[i][j] = '#'
                elif j % 4 == 2:
                    lst[i][j] = string[k]
                    k += 1

    print(f'#{t}')
    for row in lst:
        print(''.join(row))
