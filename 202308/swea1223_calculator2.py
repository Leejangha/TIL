op = {'*':2, '+':1}

for t in range(1,11):
    N = int(input())
    formula = input()
    stack = []
    susik = ''
    for char in formula:
        if char.isdigit():
            susik += char
        else:
            if len(stack) == 0 or op[stack[-1]] < op[char]:
                stack.append(char)
            elif op[stack[-1]] >= op[char]:
                while len(stack) > 0 and op[stack[-1]] >= op[char]:
                    susik += stack[-1]
                    stack.pop()
                stack.append(char)
                stack.pop()


    for char in susik:
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