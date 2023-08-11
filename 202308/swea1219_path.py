def path(n, m, v):
    stack = []
    visited = [0] * (v+1)
    visited[n] = 1
    while True:
        for w in range(1, v+1):
            if w in graph[n] and visited[w] == 0:
                stack.append(n)
                n = w
                visited[n] = 1
                if visited[m] == 1:
                    return 1
                break
        else:
            if stack:
                n = stack.pop()
            else: 
                break
    return 0


for _ in range(10):
    t, E = map(int, input().split())

    graph = [[] * 2 for _ in range(100)]
    MAP = list(map(int, input().split()))
    for i in range(E):
        graph[MAP[i*2]].append(MAP[i*2+1])

    print(f'#{t} {path(0,99,100)}')