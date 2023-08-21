# delta
d = [(1,0), (0,1), (-1,0), (0,-1)]
# testcase
for t in range(int(input())):
    # input
    N, P = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    # 최대 바이러스 제거 값
    res = 0
    # x,y 탐색
    for x in range(N):
        for y in range(N):
            # 투하 위치의 바이러스 개수
            cnt = MAP[x][y]
            # 투하 위치로 부터 1~P 범위 만큼
            for k in range(1,P+1):
                # 4방향
                for dx, dy in d:
                    nx, ny = x+dx*k, y+dy*k
                    # 마을안 범위
                    if 0 <= nx < N and 0 <= ny < N:
                        # 백신 폭발 범위 내의 바이러스 더함
                        cnt += MAP[nx][ny]
            # 투하 위치의 바이러스 총 제거 개수를 이전 투하위치까지의 최대값과 비교, 갱신
            if cnt > res:
                res = cnt

    print(f'#{t+1} {res}')
