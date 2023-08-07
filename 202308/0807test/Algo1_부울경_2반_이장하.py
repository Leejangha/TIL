T = int(input())

for t in range(1, T + 1):
    N = int(input())
    # 좌표 입력
    x1, y1, x2, y2 = map(int, input().split())

    # 전체 MAP 입력
    MAP = []
    for _ in range(N):
        MAP.append(list(map(int, input().split())))

    # 평지를 만드려는 영역의 넓이와 총합, 평균값 계산
    total_ground = (x2+1-x1) * (y2+1-y1)
    total_sum = 0
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            total_sum += MAP[x][y]
    avr = total_sum // total_ground

    # 평탄화 작업
    flat = 0
    # 평지의 영역만큼 반복
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            # 해당 영역의 높이가 평균이 될 때 까지 반복
            while MAP[x][y] != avr:
                # 높이가 평균보다 높을 경우 높이를 1씩 낮추며 평탄화
                if MAP[x][y] > avr:
                    MAP[x][y] -= 1
                    flat += 1
                # 높이가 평균보다 낮을 경우 높이를 1씩 높이며 평탄화
                else:
                    MAP[x][y] += 1
                    flat += 1

    print(f'#{t} {flat}')
