import sys
from collections import deque


def bfs(n):
    q = deque()
    q.append(n)
    visited[n] = True
    while q:
        now = q.popleft()
        for next in MAP[now]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
    res = visited.count(True) - 1
    return res


N = int(sys.stdin.readline())
V = int(sys.stdin.readline())
MAP = [[] for _ in range(N+1)]
for _ in range(V):
    v1, v2 = map(int, sys.stdin.readline().split())
    MAP[v1].append(v2)
    MAP[v2].append(v1)
visited = [False] * (N+1)
print(bfs(1))
