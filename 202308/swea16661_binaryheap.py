def min_heap(p):
    i = 1
    while i < N and tree[i] < tree[i//2]:
        # if tree[i] < tree[i//2]:
        tree[i], tree[i//2] = tree[i//2], tree[i]
        i += 1


for t in range(int(input())):
    N = int(input())
    lst = list(map(int, input().split()))
    tree = [0] + lst
    min_heap(N)
    k = N // 2
    res = 0
    while k:
        res += tree[k]
        k //= 2

    print(f'#{t+1} {res}')
