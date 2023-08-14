T = int(input())

#괄호검사
def check(formular): #괄호검사
    stack = [0] * 100
    sp = -1

    for form in formular:
        if form in ['(', '{']: #여는 괄호 push
            sp += 1
            stack[sp] = form
        elif form == ')':
            if sp >= 0 and stack[sp] == '(':
                sp -= 1
            else:
                return 0
        elif form == '}':
            if sp >= 0 and stack[sp] == '{':
                sp -= 1
            else:
                return 0
    if sp >= 0:
        return 0
    return 1

#괄호가 정상인 수식들만
def calculate(formular):
    stack = [0] * 100
    sp = -1

    for form in formular:
        if form not in [')', '}']: #숫자나, 여는괄호 push
            sp += 1
            stack[sp] = form

        elif form == ')':
            temp = 0
            while sp > -1 and stack[sp] != '(':
                temp += int(stack[sp])
                sp -= 1 # pop하기
            sp -= 1 # '(' pop
            sp += 1
            stack[sp] = temp #연산결과 push

        elif form == '}':
            temp = 1
            while sp > -1 and stack[sp] != '{':
                temp *= int(stack[sp])
                sp -= 1 # pop하기
            sp -= 1 # '{' pop
            sp += 1
            stack[sp] = temp #연산결과 push

    if sp != 0:
        return -1
    else:
        return stack[sp]




for t in range(1,T+1):
    formular = input()
    ans = -1

    if check(formular):
        ans = calculate(formular)

    print(f'#{t} {ans}')
