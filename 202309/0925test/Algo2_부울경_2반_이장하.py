def games(n, score):
    global max_score

    if n == N:
        return

    for y in range(N):
        if not visited[y]:
            visited[y] = True
            score += targets[n][y]
            games(n+1, score)
    if score > max_score:
        max_score = score


for t in range(int(input())):
    N = int(input())
    targets = [list(map(int, input().split())) for _ in range(N)]
    max_score = 0
    visited = [False] * (N+1)
    games(0, 0)

    print(f'#{t+1} {max_score}')
