N = 1
S = 2

for t in range(10):
    input()
    table = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0
    for y in range(100):
        x = 0
        while 0 <= x < 100:
            if table[x][y] == N:
                i = x+1
                while i < 100:
                    if table[i][y] == S:
                        cnt += 1
                        x = i+1
                        break
                    else:
                        i += 1
                x = i
            else:
                x += 1

    print(f'#{t+1} {cnt}')
