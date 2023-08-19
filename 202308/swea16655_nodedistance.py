def bfs(s, g, v):
    q = []
    q.append(s)
    visited = [0] * (v+1)

    while q:
        s = q.pop(0)
        for w in range(1, v+1):
            if edges[s][w] == 1 and visited[w] == 0:
                q.append(w)
                visited[w] += visited[s] + 1
    return visited[g]


for t in range(int(input())):
    V, E = map(int, input().split())
    edges = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        v1, v2 = map(int, input().split())
        edges[v1][v2] = 1
        edges[v2][v1] = 1
    S, G = map(int, input().split())
    res = bfs(S, G, V)
    print(f'#{t+1} {res}')
