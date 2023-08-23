op = ['+', '-', '*', '/']


def oper(p):
    while p <= N:
        if tree[p] in op:
            if tree[L[p]] not in op and tree[R[p]] not in op:
                if tree[p] == '+':
                    tree[p] = tree[L[p]] + tree[R[p]]
                elif tree[p] == '-':
                    tree[p] = tree[L[p]] - tree [R[p]]
                elif tree[p] == '*':
                    tree[p] = tree[L[p]] * tree[R[p]]
                elif tree[p] == '/':
                    tree[p] = tree[L[p]] / tree[R[p]]
                p -= 1
            elif tree[L[p]] in op:
                oper(L[p])
            elif tree[R[p]] in op:
                oper(R[p])
        p += 1


for t in range(1,11):
    N = int(input())
    tree = [0]*(N+1)
    L = [0]*(N+1)
    R = [0]*(N+1)
    for _ in range(N):
        lst = list(input().split())
        node = int(lst[0])
        if lst[1] in op:
            tree[node] = lst[1]
        else:
            tree[node] = float(lst[1])
        if len(lst) == 4:
            l, r = map(int, lst[2:])
            L[node] = l
            R[node] = r
        elif len(lst) == 3:
            l = int(lst[2])
            L[node] = l

    oper(1)

    if tree[1] in op:
        if tree[1] == '+':
            tree[1] = tree[L[1]] + tree[R[1]]
        elif tree[1] == '-':
            tree[1] = tree[L[1]] - tree[R[1]]
        elif tree[1] == '*':
            tree[1] = tree[L[1]] * tree[R[1]]
        elif tree[1] == '/':
            tree[1] = tree[L[1]] / tree[R[1]]
    res = int(tree[1])

    print(f'#{t} {res}')
