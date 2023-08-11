T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    MAP += list(zip(*MAP))

    max_length = 0
    for row in MAP:
        length = 0
        for char in row:
            if char == 1:
                length += 1
            else:
                if length > max_length:
                    max_length = length
                    length = 0
        if length > max_length:
            max_length = length

    print(f'#{t} {max_length}')
