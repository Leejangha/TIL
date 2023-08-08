T = int(input())

for t in range(1, T+1):
    MAP = [list(map(int, input().split())) for _ in range(9)]
    MAP.extend([x for x in zip(*MAP)])

    cnt = 0
    for x in range(18):
        if len(set(MAP[x])) == 9:
            cnt += 1

    for x in range(3):
        for y in range(3):
            lst = []
            for i in range(3):
                for j in range(3):
                    lst.append(MAP[3*x+i][3*y+j])
            if len(set(lst)) == 9:
                cnt += 1

    if cnt == 27:
        res = 1
    else:
        res = 0

    print(f'#{t} {res}')
