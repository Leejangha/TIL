for t in range(1,11):
    N = int(input())
    formula = input()
    res = 0
    stack = []
    op = []
    for form in formula:
        if form != '+':
            stack.append(int(form))
        else:
            op.append(form)
    while op:
        op.pop()
        res += stack[-1]
        stack.pop()
    print(f'#{t} {res}')
