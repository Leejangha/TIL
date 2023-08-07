for t in range(1, 11):
    N = int(input())

    MAP = [list(input()) for _ in range(8)]

    cnt = 0

    for x in range(8):
        for y in range(9-N):
            is_palin = 0
            for j in range(N//2):
                if MAP[x][y+j] == MAP[x][y+N-1-j]:
                    is_palin += 1
                else:
                    is_palin = 0
            if is_palin == N//2:
                cnt += 1

    for y in range(8):
        for x in range(9-N):
            is_palin = 0
            for i in range(N // 2):
                if MAP[x+i][y] == MAP[x+N-1-i][y]:
                    is_palin += 1
                else:
                    is_palin = 0
            if is_palin == N // 2:
                cnt += 1

    print(f'#{t} {cnt}')
