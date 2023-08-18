import sys
from collections import deque

def bfs(s, g, v):
    q = deque([])
    q.append(s)
    visited = [0] * (v+1)

    while q:
        s = q.popleft()
        for w in MAP[s]:
            if visited[w] == 0:
                q.append(w)
                if visited[s] < g:
                    visited[w] = visited[s] + 1
    return visited


N, M, K, X = map(int, sys.stdin.readline().split())
MAP = [[] for _ in range(N+1)]
for i in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    MAP[v1].append(v2)
res = bfs(X, K, N)
res.sort()

flag = False
for i in range(N+1):
    if res[i] == K:
        print(i)
        flag = True

if not flag:
    print(-1)
