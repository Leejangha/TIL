import sys
from collections import deque

input = sys.stdin.readline

N, M, R = map(int, input().split())
MAP = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    MAP[u].append(v)
    MAP[v].append(u)
for i in range(N+1):
    MAP[i].sort(reverse=True)

def bfs(V, R):
    q = deque([])
    visited = [0] * (N+1)
    cnt = 1
    visited[R] = cnt
    q.append(R)

    while q:
        now = q.popleft()
        for next in V[now]:
            if visited[next] == 0:
                cnt += 1
                visited[next] = cnt
                q.append(next)
    for i in range(1,N+1):
        print(visited[i])

bfs(MAP, R)
