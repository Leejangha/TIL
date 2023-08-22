def node(N):
    stack = []
    visited = [0] * (N + 1)
    now = 1
    stack.append(1)
    visited[1] = 1
    idx = []
    res = ''

    while True:
        for next in range(1, N+1):
            if next in MAP[now] and visited[next] == 0:
                stack.append(next)
                now = next
                visited[next] = 1

        else:
            if stack:
                now = stack.pop()
            else:
                break
        idx.append(now)

    for i in idx:
        res += string[i-1]
    return res


for t in range(1, 11):
    N = int(input())
    lst = [input().split() for _ in range(N)]
    MAP = [[] for _ in range(N+1)]
    string = []
    for i in lst:
        char = i[1]
        string.append(char)
        N = int(i[0])
        if len(i) == 4:
            L, R = map(int, i[2:])
            MAP[N].extend([L,R])
        elif len(i) == 3:
            L = int(i[2])
            MAP[N].append(L)

    print(f'#{t} {node(N)}')


# 풀이
def inorder(p):  # N 완전이진트리의 마지막 정점
    if p <= N:
        inorder(p*2)    # 왼쪽 자식으로 이동
        print(tree[p], end='')  # 중위순회에서 할 일
        inorder(p*2+1)  # 오른쪽 자식으로 이동


T = 10
for t in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    for _ in range(N):
        arr = list(input().split())
        tree[int(arr[0])] = arr[1]
    # 중위순회
    print(f'#{t} ', end='')
    inorder(1)   # root = 1
    print()
