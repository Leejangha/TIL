def inorder(tree):
    def _inorder(tree, i=0):
        if i >= len(tree) or tree[i] is None:
            return
        left = 2*i+1
        right = left+1
        _inorder(tree, left)
        res.append(tree[i])
        _inorder(tree, right)

    res = []
    _inorder(tree)
    return res


for t in range(int(input())):
    N = int(input())
    tree = list(range(1,N+1))
    ans = inorder(tree)
    result = [0] * N
    j = 1
    for i in ans:
        result[i-1] = j
        j += 1
    res1 = result[0]
    res2 = result[N//2-1]
    print(f'#{t+1} {res1} {res2}')
