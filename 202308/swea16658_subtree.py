def node(N):
    visited = [0]*(E+2)
    stack = []
    stack.append(N)
    visited[N] = 1
    cnt = 1
    while stack:
        now = stack.pop()
        for next in tree[now]:
            if visited[next] == 0:
                visited[next] = 1
                cnt += 1
            stack.append(next)
    return cnt


for t in range(int(input())):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    tree = [[]*2 for _ in range(E+2)]
    for i in range(0, E*2, 2):
        tree[lst[i]].append(lst[i+1])
    res = node(N)
    print(f'#{t+1} {res}')
