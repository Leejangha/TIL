def min_heap(i):
    while i > 1:
        if tree[i] < tree[i//2]:
            tree[i], tree[i//2] = tree[i//2], tree[i]
            i //= 2
        else:
            break

for t in range(int(input())):
    N = int(input())
    lst = list(map(int, input().split()))
    tree = [0] + lst
    for i in range(1,N+1):
        min_heap(i)
    res = 0
    k = N // 2
    while k > 0:
        res += tree[k]
        k //= 2

    print(f'#{t+1} {res}')
