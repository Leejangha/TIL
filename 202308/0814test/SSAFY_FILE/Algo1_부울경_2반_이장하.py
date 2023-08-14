d = [(0,1), (-1,0), (0,-1), (1,0)]

for t in range(int(input())):
    N = int(input())
    # 높이의 외각을 0으로 둘러쌈
    h = [[0]*(N+2) for _ in range(N+2)]
    for i in range(1, N+1):
        h[i][1:N+1] = list(map(int, input().split()))
    # 봉우리의 개수 초기화
    cnt = 0
    for x in range(1, N+1):
        for y in range(1, N+1):
            # (1,1) 부터 (N+1,N+1)가지 탐색
            high = h[x][y]
            # 봉우리일 경우 True
            is_high = True
            # 4방향 탐색
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                # 탐색하는 곳의 높이가 4방향의 높이보다 하나라도 작을 경우 False
                if high <= h[nx][ny]:
                    is_high = False
            # 봉우리일 경우 cnt + 1
            if is_high:
                cnt += 1

    print(f'#{t+1} {cnt}')

#
T = int(input())

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

for t in range(1,T+1):
    N = int(iuput())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0

    for r in range(N):
        for c in range(N):
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < N and 0 <= nc < N:
                    if MAP[r][c] <= MAP[nr][nc]:
                        break
            else:
                cnt += 1

    print(f'#{t} {cnt}')
