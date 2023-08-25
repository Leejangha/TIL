op = ['+', '-', '*', '/']


def oper(p):
    while p <= N:
        if tree[p] in op:
            if tree[L[p]] in op:
                oper(L[p])
            elif tree[R[p]] in op:
                oper(R[p])
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
    res = int(tree[1])

    print(f'#{t} {res}')

# 하드코딩
for t in range(1,11):
    N = int(input())
    lst = [list(input().split()) for _ in range(N)]
    lst = [0] + lst

    for i in range(N, 0, -1):
        if lst[i][1] in '+-*/':
            if lst[i][1] == '+':
                lst[i] = (i, int(lst[int(lst[i][2])][1]) + int(lst[int(lst[i][3])][1]))
            elif lst[i][1] == '-':
                lst[i] = (i, int(lst[int(lst[i][2])][1]) - int(lst[int(lst[i][3])][1]))
            elif lst[i][1] == '*':
                lst[i] = (i, int(lst[int(lst[i][2])][1]) * int(lst[int(lst[i][3])][1]))
            else:
                lst[i] = (i, int(lst[int(lst[i][2])][1]) / int(lst[int(lst[i][3])][1]))

    result = int(lst[1][1])

    print(f'#{t} {result}')

# 2차
def postOrder(v):
    if v:
        postOrder(left[v])
        postOrder(right[v])
        
        if tree[v] == '-':
            tree[v] = int(tree[left[v]]) - int(tree[right[v]])
        elif tree[v] == '/':
            tree[v] = int(tree[left[v]]) / int(tree[right[v]])
        elif tree[v] == '*':
            tree[v] = int(tree[left[v]]) * int(tree[right[v]])
        else:
            tree[v] = int(tree[left[v]]) + int(tree[right[v]])


for t in range(1, 11):
    N = int(input())
    tree = [0]*(N+1)
    left = [0]*(N+1)
    right = [0]*(N+1)

    for _ in range(N):
        lst = input().split()
        tree[int(lst[0])] = lst[1]

        if len(lst) == 4:
            left[int(lst[0])] = int(lst[2])
            right[int(lst[0])] = int(lst[3])

        if len(lst) == 3:
            left[int(lst[0])] = int(lst[2])

    postOrder(1)

    print(f'#{t}')