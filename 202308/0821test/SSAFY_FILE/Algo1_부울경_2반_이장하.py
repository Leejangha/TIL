# delta
d = [(0,1), (1,0), (0,-1), (-1,0)]
# testcase
T = int(input())

for t in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    max_point = 0
    min_point = 9*N*2

    for x in range(N):
        for y in range(N):
            # 터트린 풍선의 숫자를 점수에 더함
            K = MAP[x][y]
            point = K
            # 처음 터트린 풍선의 숫자만큼 4방향으로 풍선을 터트려 점수에 더함
            for k in range(1, K+1):
                for dx, dy in d:
                    nx, ny = x+dx*k, y+dy*k
                    if 0 <= nx < N and 0 <= ny < N:
                        point += MAP[nx][ny]
            # 한번 터트렸을때 점수를 현재 까지의 최대, 최소 점수와 비교해가며 최신화함
            if point > max_point:
                max_point = point
            if point < min_point:
                min_point = point
    # 결과는 최대점수와 최소점수의 차이
    res = max_point - min_point

    print(f'#{t} {res}')
