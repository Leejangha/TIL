# testcase
for t in range(int(input())):
    # input
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    # 크키가 최대인 사각형의 넓이, 개수
    max_s = 0
    cnt = 0
    # 게임판 전체 탐색
    for x in range(N):
        for y in range(N):
            # 탐색 위치의 숫자
            num = MAP[x][y]
            # 게임판의 마지막 칸부터 탐색
            for i in range(N-1, x-1, -1):
                for j in range(N-1, y-1, -1):
                    # 탐색 시작 위치부터 같은 숫자가 있는 위치 까지의 넓이
                    if MAP[i][j] == num:
                        s = 0
                        # num 부터 MAP[ni][nj]까지의 넓이가 현재 최대 값보다 작을 경우 계산할 필요가 없음
                        if (i+1-x) * (j+1-y) >= max_s:
                            s = (i+1-x)*(j+1-y)
                            # 넓이가 최대 넓이와 같을 경우 개수 +1
                            if s == max_s:
                                cnt += 1
                            # 넓이가 최대 넓이 보다 클 경우 갱신
                            elif s > max_s:
                                max_s = s
                                cnt = 1

    print(f'#{t+1} {cnt}')
