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


# 수정
def inorder(p):  # N 완전이진트리의 마지막 정점
    global i
    if p <= N:
        inorder(p*2)    # 왼쪽 자식으로 이동
        tree[p] = i     # 중위순회에서 할 일
        i += 1
        inorder(p*2+1)  # 오른쪽 자식으로 이동


T = int(input())
for t in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    i = 1
    inorder(1)

    # 중위순회
    print(f'#{t} {tree[1]} {tree[N//2]}')
