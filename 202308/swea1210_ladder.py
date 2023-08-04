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


T = 10
for t in range(1, T+1):
    input()

    MAP = list(map(int, input().split))

    # 도착점부터
    for n in range(100):
        if MAP[99][n] == 2:
            x = n
            break
    
    # 출발점
    y = 99

    while True:
        # 출발점에 도착하면 끝내겠다
        if y == 0:
            break

        # 맵의 오른쪽을 벗어나지 않으면서 + 오른쪽에 값 존재하는 경우
        if x < 99 and MAP[y][x+1]:
            while x < 99 and MAP[y][x+1]:
                x += 1
        
            else:
                y -= 1

        # 왼쪽 로직 오른쪽을 복사해서 일부만 바꾼다
        elif x > 0 and MAP[y][x-1]:
            while x > 0 and MAP[y][x-1]:
                x -= 1
        
            else:
                y -= 1
        
        else:
            y -= 1

    print(f'#{t} {x}')