def bfs(s, v):
    visited = [0]*(101)
    q = []
    q.append(s)
    visited[s] = 1
    while q:
        n = q.pop(0)
        for w in phones[n]:
            if visited[w] == 0:
                q.append(w)
                visited[w] += visited[n] + 1
    return visited


for t in range(10):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    phones = [[] for _ in range(101)]
    for i in range(0, N-1, 2):
        v1 = lst[i]
        v2 = lst[i+1]
        phones[v1].append(v2)

    res = bfs(S, N)
    ans = 0

    for i in range(101):
        if res[i] == max(res) and i >= ans:
            ans = i

    print(f'#{t+1} {ans}')
