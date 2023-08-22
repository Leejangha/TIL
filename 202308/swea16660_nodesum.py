def postorder(p):
    if p<=N:
        postorder(p*2)
        postorder(p*2+1)
        tree[p//2] += tree[p]


for t in range(int(input())):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        tree[a] = b
    postorder(1)

    print(f'#{t+1} {tree[L]}')
