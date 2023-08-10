T = int(input())


def dfs(n, g, v):
    stack = []
    visited = [0] * (v+1)
    visited[n] = 1
    while True:
        for w in range(1, v+1):
            if graph[n][w] == 1 and visited[w] == 0:
                stack.append(n)
                n = w
                visited[n] = 1
                if visited[g] == 1:
                    return 1
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break
    return 0


for t in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        v1, v2 = map(int, input().split())
        graph[v1][v2] = 1
    S, G = map(int, input().split())

    print(f'#{t} {dfs(S, G, V)}')
