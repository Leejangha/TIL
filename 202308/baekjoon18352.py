import sys
from collections import deque

def bfs(s, g, v):
    q = deque([])
    q.append(s)
    visited = [0] * (v+1)
<<<<<<< HEAD
    visited[n] = 1
    l = [0] * (v+1)
    while True:
        dis = 0
        for w in range(1, v+1):
            if MAP[n][w] == 1 and visited[w] == 0:
                stack.append(n)
                n = w
                visited[n] = 1
                dis += 1
                if dis == g:
                    l[n] = 1
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break
    return l


N, M, K, X = map(int, input().split())
MAP = [[0] * (N+1) for _ in range(N+1)]
for i in range(M):
    v1, v2 = map(int, input().split())
    MAP[v1][v2] = 1
res = dfs(X, K, N)

found = False
for i in range(N):
    if res[i] == 1:
        print(i)
        found = True

if not found:
    print(-1)
=======

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
>>>>>>> 3369968bbccef107b4009bb25661e57df2fdfaec
