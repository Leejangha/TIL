import sys
from collections import deque

def bfs(s, g):
    q = deque([])
    q.append(s)
    visited[s] = True
    res = []

    while q:
        n = q.popleft()
        for w in MAP[n]:
            if not visited[w]:
                visited[w] = True
                q.append(w)
                dis[w] = dis[n] + 1
                if dis[w] == g:
                    res.append(w)

    if len(res) == 0:
        print(-1)
    else:
        res.sort()
        for i in res:
            print(i, end = '\n')


N, M, K, X = map(int, sys.stdin.readline().split())
MAP = [[] for _ in range(N+1)]
for i in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    MAP[v1].append(v2)
visited = [False] * (N+1)
dis = [0] * (N + 1)

bfs(X, K)
