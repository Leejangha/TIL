op = {'*': 2, '+': 1}

for t in range(1,11):
    N = int(input())
    formula = input()
    stack = []
    operator = []
    for char in formula:
        if char.isdigit():
            operator.append(char)
        else:
            if stack and op[char] <= op[stack[-1]]:
                operator.append(stack.pop())
            stack.append(char)
    while stack:
        operator.append(stack.pop())

    for char in operator:
        if char.isdigit():
            stack.append(int(char))
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            if char == '+':
                stack.append(op1 + op2)
            elif char == '*':
                stack.append(op1 * op2)

    print(f'#{t} {stack[-1]}')
