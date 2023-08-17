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


# 수정
T = 10
for t in range(1,T+1):
    input()
    STR = input()
    STACK = []
    postfix = ''
    for s in STR:
        #숫자인경우 후위표기식에 추가
        if s.isdecimal():
            postfix += s
        else:
            while STACK and STACK[-1] == '*':
                postfix += STACK.pop()
            STACK.append(s)
    
    while STACK:
        postfix += STACK.pop()
    
    result = []

    for p in postfix:
        if p.isdecimal():
            result.append(int(p))
        else:
            num2 = result.pop()
            num1 = result.pop()
            if p == '+':
                result.append(num1 + num2)
            elif p == '*':
                result.append(num1 * num2)
    print(f'#{t}', *result)