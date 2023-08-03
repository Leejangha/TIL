j = 0
i = 99
ladders = [list(map(int, input().split())) for _ in range(100)]
ladders[99][0] = 1
if j>0 and ladders[i][j-1]:
    print('a')