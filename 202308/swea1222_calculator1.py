for t in range(1,11):
    N = int(input())
    formula = input()
    stack = []
    op = []
    for form in formula:
        if form != '+':
            stack.append(int(form))
        else:
            op.append(form)
    while op:
        op1 = stack[-1]
        stack.pop()
        op2 = stack[-1]
        stack.pop()
        stack.append(op1 + op2)
        op.pop()

    print(f'#{t} {stack[-1]}')
