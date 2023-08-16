op = ['+', '-', '*', '/']


def forth(formula):
    stack = []
    for char in formula:
        if char == '.':
            if len(stack) == 1:
                return stack[-1]
            else:
                return 'error'
        elif char not in op:
            stack.append(int(char))
        elif char in op:
            if len(stack) >= 2:
                op2 = stack[-1]
                stack.pop()
                op1 = stack[-1]
                stack.pop()
                if char == '+':
                    stack.append(op1 + op2)
                elif char == '-':
                    stack.append(op1 - op2)
                elif char == '*':
                    stack.append(op1 * op2)
                elif char == '/':
                    if op2 == 0:
                        return 'error'
                    else:
                        stack.append(op1 // op2)
            else:
                return 'error'


for t in range(int(input())):
    formula = input().split()
    print(f'#{t+1} {forth(formula)}')
