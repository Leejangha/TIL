for _ in range(10):
    t = int(input())
    ladders = []
    for _ in range(100):
        ladders.append(list(map(int, input().split())))
    start = ladders[99].index(2)

    i, j = 99, start
        while i > 0:
            if j != 0 and ladders[i][j - 1] == 1:
                while j > 0:
                    j -= 1
                    if j == 0 or ladders[i][j - 1] == 0:
                        i -= 1
                        break
            elif j != 99 and ladders[i][j + 1] == 1:
                while j < 99:
                    j += 1
                    if j == 99 or ladders[i][j + 1] == 0:
                        i -= 1
                        break
            else:
                while i > 0:
                    i -= 1
                    if j == 99 or ladders[i][j + 1] == 1:
                        break
                    if j == 0 or ladders[i][j - 1] == 1:
                        break

    print(f'#{t} {j}')

# GPT
for _ in range(10):
    t = int(input())
    ladders = [list(map(int, input().split())) for _ in range(100)]
    start = ladders[99].index(2)

    i, j = 99, start
    while i > 0:
        if j > 0 and ladders[i][j - 1]:
            while j > 0 and ladders[i][j - 1]:
                j -= 1
            i -= 1
        elif j < 99 and ladders[i][j + 1]:
            while j < 99 and ladders[i][j + 1]:
                j += 1
            i -= 1
        else:
            i -= 1

    print(f'#{t} {j}')
